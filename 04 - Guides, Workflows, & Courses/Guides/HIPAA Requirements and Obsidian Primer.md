---
aliases: 
- Protected Health Information and Obsidian
tags:
- evergreen
publish: true
---

# HIPAA Requirements and Obsidian Primer

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

This article aims to give an overview of using [[Obsidian]] for protected health information in a medical context, giving advice on the [[Plugins for Security and Privacy|security and privacy]] of patient data with regard to the Health Insurance Policy and Accountability Act of 1996 (HIPAA).

Author: [Valmeek Kudesia](https://www.linkedin.com/in/valmeekkudesia), MD (Board Certified Internal Medicine, Board Certified Clinical Informatics)

Last updated: 2022-02-28

## TL; DR:
*Should* one use Obsidian to store and manipulate [protected health information (PHI)](https://www.hhs.gov/answers/hipaa/what-is-phi/index.html)? No, as of this document's date.

Is it *technically* possible to use Obsidian in a manner that is compliant with HIPAA regulations? Yes, but only in the context of *many* additional significant safeguards and controls that must be independently maintained, as of this document's date.

If such degree of safeguards and controls were enacted, then any "document" editor (e.g. Notepad, Microsoft Word and Excel, gedit, Emacs, vim) *could* be used in a HIPAA-compliant manner.

## Briefly, what is HIPAA?
The [Health Insurance Policy and Accountability Act (HIPAA)](https://www.cdc.gov/phlp/publications/topic/hipaa.html) is a federal law that sets forth minimum requirements for the responsible handling of a person's protected health information (PHI). These minimum requirements include, but are not limited to, audit upkeep, access control, data protection and disaster recovery, and services available to the person to whom the PHI belongs.

## Briefly, what is PHI?
Protected health information (PHI) - any information regarding health status, provision of healthcare, and payment for healthcare that can be linked to an individual, e.g. clinician visits, medication orders, diagnoses lists, laboratory results, treatment plans. This range includes medical, surgical, behavioral health domains, regardless of the clinician license e.g. a licensed social worker (LICSW) may not document in a health record; however that LICSW may have access to sensitive information describing substance abuse treatments which is covered by HIPAA regulations.

General biology or medical content is NOT considered PHI. For example, content describing the general biologic process of a myocardial infarction (heart attack) is NOT PHI. However, describing the myocardial infarction of a specific patient, "Mr Smith", IS PHI.

## Ownership and Control of PHI
PHI belongs to the person whom it describes, not the provider or holder of the PHI. For example above, any information specific to Mr Smith's heart attack is OWNED BY Mr Smith regardless of which cardiologist (heart doctor) performed the imaging test or typed the doctor notes. Therefore, Mr Smith is entitled to certain controls (or rules) that govern how his PHI is used, stored, and transmitted. HIPAA regulations provide minimum requirements for holders of PHI such that Mr. Smith is not deprived of his entitled rights over his PHI.

## Why Recommend Against Obsidian for PHI?
Obsidian's "native" philosophy is that the user of Obsidian is the owner of data (not even a specific user), which is fundamentally opposite the requirements for PHI governance. Any program functionality, extension, or data representation will reflect Obsidian's native philosophy unless specifically modified. Fundamentally, the threshold of "good enough" handling or  protection of PHI is NOT the obsidian user; rather the threshold is elevated because "good enough" is defined by the person who owns the data and has protected rights

For example, as of this document date, Obsidian does not offer user access control. It is not possible (with native Obsidian functionality) to distinguish which changes to a document were performed by separate users.

Nearly every requirement to maintain HIPAA compliance would need to be enacted outside of Obsidian, would require dedicated maintenance, and finally would require documented processes to demonstrate adherence to regulations. Dedicated maintenance would include (but not be limited to) regular penetration testing, data access review, verification of backup viability, ongoing timely correction to or retrieval of PHI as instructed by owner of PHI or authorized agency. Such overhead is not practical in day-to-day use of typical care providers.

%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/HIPAA%20Requirements%20and%20Obsidian%20Primer.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/HIPAA%20Requirements%20and%20Obsidian%20Primer.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
