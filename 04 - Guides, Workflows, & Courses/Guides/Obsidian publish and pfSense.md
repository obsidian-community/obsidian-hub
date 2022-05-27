---
aliases:
- 
tags:
- seedling
publish: true
---

# Obsidian publish and pfSense

This document describes the steps that can be taken in order to configure [[Obsidian Publish]] to use a custom domain with [[pfSense]] + [[HAProxy]] + [[Let's Encrypt]].

## Requirements

- Obsidian Publish subscription
- pfSense
- HAProxy package installed
- Acme package installed
- DNS record for your custom domain pointing to the pfSense public IP address
- Ports 80 and 443 open in pfSense firewall

There is already a lot of documentation available for setting up a pfSense installation with HAProxy, so I will not cover that.

The Acme package will be used for automatic certificate management from Let's Encrypt.

The firewall settings for WAN interface should be something like below

![[publish-pfsense-fw.png]]

## ACME configuration

After installing the Acme package, head over to **Services -> Acme certificates**

![[publish-pfsense-acme_1.png]]

Choose **Account keys** and click _+ Add_.

![[publish-pfsense-acme_2.png]]

For your new account

- set _Name_ and _Description_, which are only visible in the pfSense
- set the ACME Server to **Let's Encrypt Production ACME v2**
- type an email address to be associated with this account
- click **+ Create new account key**
- click _Register ACME Account Key_ and save your settings after registration succeeds.

Your ACME account is now setup, but you cannot request for certificates yet. Let's setup the HAproxy [[Obsidian publish and pfSense#HTTP Frontend|HTTP Frontend]] first.

---

After you've setup the HTTP frontend, return to the _Acme certificates_ service and choose the _Certificates_ -tab. Click on _+ Add_ to request for a new certificate.

For the new certificate, set the name (and description). For the name, I recommend to follow a naming syntax of for example `cert-<domain_name>`. For this domain, the name would be `cert-tkjt.dev`. Make sure _Status_ is set to _Active_ and the _Acme Account_ is the one you previously created (should be by default if you have only one). Choose the desired _Private Key_ setting. For my personal site, I've settled for the `2048-bit RSA`, which is still considered "secure enough".

![[publish-pfsense-acme_3.png]]

Scroll down and set the _Domain SAN list_ settings. You can configure multiple domain names if you like, but I usually keep it to 1 domain / 1 certificate.

Set the **Domain name** to your domain, and **Method** to _Webroot local folder_, for example

![[publish-pfsense-acme_4.png]]

The value for the **Root Folder** should be set to

```
/tmp/haproxy_chroot/.well-known/acme-challenge/
```

The certificate is renewed by default every **60 days**, but the new certificate will not activate until HAProxy is restarted, so you probably want to add an action for that in the _Actions list_. Click _+ Add_ and set the following

![[publish-pfsense-acme_5.png]]

The value in the **Command** field should be set to

```
/usr/local/etc/rc.d/haproxy.sh restart
```

Click on _Save_.

The certificte configuration is now available. To Issue your first certificate, click on _Issue/Renew_ and wait about a minute. If everything is setup properly, a new certificate should be successfully issued (see the log displayed at the top of the page).

The certificate is now available for use in pfSense and should automatically renew every **60 days**.

## HAProxy configuration

### Frontends

You will need atleast two frontends for HAProxy, but I recommend a setup of three. Two primary frontends, listening on ports 80 and 443, and a third one for providing the actual service(s).

The HTTP Frontend (port 80) will be used for the certificate validation and redirecting all clients to https. HTTPS Frontend (port 443) is for the actual service(s).

#### HTTP Frontend

Open **Services -> HAProxy** and select **Frontend** -tab. Click _Add_.

Choose a **Name** and **Description**, for example _HTTP_Default_ and _HTTP frontend_. Make sure status is set to _Active_.

> **Name** cannot contain any white spaces and special character selection is limited

The **External address** should be configured to use **Listen address** `WAN address` and **Port** `80` like below

![[publish-pfsense-http-fe_1.png]]

Scroll down the page and set the following options for _Access control lists_

| Name              | Expression        | Not | Value                          |
| ----------------- | ----------------- | --- | ------------------------------ |
| `url_acme_http01` | Path starts with: | no  | `/.well-known/acme-challenge/` |
| `no_ssl`          | Custom acl:       | yes | `ssl_fc`                       |

![[publish-pfsense-http-fe_2.png]]

The first ACL sets a condition indicating a request for ACME certificate validation and the second a flag indicating is SSL was enabled or not.

Scroll a bit further and set the following actions

| Action                     | Parameters                            | Condition acl names Value |
| -------------------------- | ------------------------------------- | ------------------------- |
| `http-request lua service` | lua-function: `acme-http01`           | METH_GET url_acme_http01  |
| `Custom`                   | customaction: `redirect scheme https` | no_ssl                    |

![[publish-pfsense-http-fe_3.png]]

The first action is for Let's Encrypt's domain validation used in certificate issuing and it checks for HTTP request type `GET` and a request path matching the one defined in ACL `url_acme_http01`. The second will redirect all other clients to use your HTTPS backend instead.

Other options can be left as is.

Click _Save_ and apply the configuration changes on the next page

![[publish-pfsense-http-fe_4.png]]

#### HTTPS Frontends

For HTTPS, we will configure two frontends. The first is the actual frontend where we define SSL certificates and do some simple hardening.

Open **Services -> HAProxy** and select **Frontend** -tab. Click _Add_.

Choose a **Name** and **Description**, for example _HTTPS_Default_ and _Generic SSL Frontend_. Make sure status is set to _Active_.

Set the **Listen address** to `WAN address`, **Port** to `443` and check **SSL Offloading**. I've also set the **Max connections** to `2048`.

![[publish-pfsense-https-fe_1.png]]

If you want, you can setup some simple hardening of your environment with for example the following actions

![[publish-pfsense-https-fe_2.png]]

These will start rejecting connections from clients sending an excessive number of requests to your site or try to communicate without SSL to the port `443`.

The `host_is_lb` and `host_is_ip` are ACL's configured to match the name of the Firewall itself and any IP address, which I just want to have a separate actions for. The admin ui is not available through WAN interface by default, so this is not absolutely necessary, but I just like to always configure HAProxy to explicitly block these.

The last one enforces `SameSite=Lax` setting for _all_ cookies set by any service behind this HAProxy instance. See [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite) for details.

In the _Advanced settings_ I recommend you set the **httpclose** option to `http-server-close`

![[publish-pfsense-https-fe_3.png]]

Scroll down to _SSL Offloading_ and choose the default certificate for HAProxy. If you only have the one certificate you just created, choose that. Otherwise, choose one of the available _server_ certificates in the list or accept the default.

In the _Additional certificates_ choose all the other certificates you want to have available for HAProxy. Here is where you choose for example the certificate you created previously. If you only have the one certificate and you chose that as the default, _you do not need to separately include the certificate here_.

![[publish-pfsense-https-fe_4.png]]

Set the **Advanced ssl options** to for example the following

```
no-sslv3 no-tlsv10 no-tlsv11 no-tls-tickets ciphers ecdhe-ecdsa-aes128-gcm-sha256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
```

Click _Save_ and apply the settings on the next page.

At this point, create the [[Obsidian publish and pfSense#Backend|backend]] for the Obsidian publish site.

Once the backend is created, create one more Frontend for actually serving content from the backend.

---

Open **Services -> HAProxy** and select **Frontend** -tab. Click _Add_.

Choose a name and description like with the first frontend, but for this one, select the _Share frontend_ and choose previously created frontend as the primary frontend

![[publish-pfsense-https-fe_5.png]]

Create an ACL matching your hostname. For me this is `tkjt.dev` (this site)

| Name            | Expression      | Not | Value      |
| --------------- | --------------- | --- | ---------- |
| `host_tkjt.dev` | Host ends with: | no  | `tkjt.dev` |

![[publish-pfsense-https-fe_6.png]]

and add an action proxying traffic from [Obsidian Publish](https://publish.obsidian.md) when a request for your host is made

| Action        | Parameters                  | Condition acl names Value |
| ------------- | --------------------------- | ------------------------- |
| `Use Backend` | backend: `Obsidian_Publish` | host_tkjt.dev             |

![[publish-pfsense-https-fe_7.png]]

Click _Save_ and apply the settings.

At this point the Backend should be available in the HAProxy status panel

![[publish-pfsense-https-fe_8.png]]

> You can add the HAProxy status panel to the front page of pfSense

Notice that in my environment, two of the backends are marked as down. This is due to them being IPv6 addresses and I have all IPv6 traffic currently blocked, which also prevents the HAProxy from checking their status. This is ok.

### Backend

Open **Services -> HAProxy** and select **Backend** -tab. Click _Add_.

The backend for Obsidian publish can use the DNS name of `publish.obsidian.md`. This automatically adds all the ip addresses the hostname resolves to as backend servers and allows for automatic failover and load balancing.

The backend can be configured with the following options

![[publish-pfsense-be_1.png]]

You can also enforce additional SSL validations, but I've just left them out for now.

The advanced setting of

```
check-sni publish.obsidian.md sni str(publish.obsidian.md) resolve-prefer ipv4
```

is required for Obsidian Publish to be usable with HAProxy as it uses [SNI](https://en.wikipedia.org/wiki/Server_Name_Indication). Without this, the backend is unable to do an SSL Handshake and the connection will not work.

In the _Access control lists and actions_ section, you must configure **Actions** like below

| Action                    | Parameters                                        | Condition acl names Value |
| ------------------------- | ------------------------------------------------- | ------------------------- |
| `http-request header set` | name: `x-obsidian-custom-domain`, fmt: `tkjt.dev` |                           |
| `http-request header set` | name: `Host`, fmt: `publish.obsidian.md`          |                           |

![[publish-pfsense-be_2.png]]

The value for `x-obsidian-custom-domain` must be the name of your custom domain. There is a mention about this in [Obsidian Help](https://help.obsidian.md/Licenses+%26+add-on+services/Obsidian+Publish#Supported+HTTP+X-Headers). As the actual request is towards the service at `publish.obsidian.md`, we need to also change the `Host` -header value for the outbound request.

> If you serve multiple Obsidian Publish sites behind this HAProxy instance with different custom domains, you must add an ACL to check for the request `Host` header value and use a condition in the Action for setting the `x-obsidian-custom-domain` header to a correct value.

Configure the health check like this

![[publish-pfsense-be_3.png]]

I've set the health check interval to 30 seconds, which IMO should be just fine for this purpose. Could also be longer but 1 request every 30 seconds should not be considered as excessive by the backend service.

**Http check version** must be set to the following value

```
HTTP/1.1\r\nHost:\ publish.obsidian.md\r\nAccept:\ */*
```

Enable HSTS and cookie protection

![[publish-pfsense-be_4.png]]

[HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) enforces clients to always use a secure connection and require a valid certificate when communicating with a site and setting the secure attribute in cookies enforces them to be only ever sent over a secure connection, ie. HTTPS.

Click _Save_ and apply the configuration changes.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Obsidian%20publish%20and%20pfSense.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/Obsidian%20publish%20and%20pfSense.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
