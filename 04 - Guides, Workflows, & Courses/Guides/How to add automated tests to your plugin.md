---
aliases: 
tags:
  - evergreen
publish: true
---

# How to add automated tests to your plugin

%% Add a description below this line. It doesn't need to be long: one or two sentences should be a good start. %%

This page will guide you through integrating [Jest](https://jestjs.io/docs/getting-started) as a testing framework to the [Obsidian example plugin](https://github.com/obsidianmd/obsidian-sample-plugin) to enable automated testing for your plugin. Furthermore, the guide will cover specialties when running tests using the Obsidian API.

This guide will use the [Obsidian example plugin](https://github.com/obsidianmd/obsidian-sample-plugin) as a showcase. It also assumes knowledge about unit testing to a certain degree. If you wish to go through the guide step-by-step, please download and enable the example plugin like described in [Build a plugin](https://docs.Obsidian.md/Plugins/Getting+started/Build+a+plugin). 

This guide focused on how to integrate Jest to your plugin and what steps to take to deal with the Obsidian API when running plugin code in a test environment. It does not provide guidance how to write test cases or what good tests are. Please refer to [[Plugin Testing for Developers]] for a deeper look at these topics as well as [[How to find examples of Jest-based plugin tests]] for examples.

## Integrate Jest into Obsidian-example-plugin

Integrating Jest to a project and make it compatible with typescript code requires some additional dependencies.

1. Open up a terminal and navigate to your plugins root folder
2. Install Jest: `npm install --save-dev jest`
3. Install types for correct typing in typescript files: `npm install --save-dev @types/jest`
4. Install ts-jest to transpile typescript files: `npm install --save-dev ts-jest`
5. Create a Jest configuration file by running `npx ts-jest config:init`
6. Open `tsconfig.json` and add `"esModuleInterop": true` as an additional property to `compilerOptions` 
7. Open `package.json` and add `"test": "jest"` to the `scripts` section 

Jest is now integrated into the project and usable for testing.

## Executing a first automated test

> [!hint] Structuring with folders
> For reason of simplicity, this guide adds files to the root folder. Generally, it is a good idea to structure your code in folders, i.e. productive code in `src` and tests in `tests` to keep your code base better maintainable. 

1. Create a new file named `example.spec.ts` to your projects root folder

> [!info] Test file names
> It is not required to call tests with a `.spec.ts` ending, `.ts` is enough. However, it allows you to see at one glance which file contain productive code and which are test files, which will help with development and maintainability. It is also common to end test file names with `.test.ts` instead of `.spec.ts`.

2. In `example.spec.ts`, add a `describe` block. Read more about describe blocks in [Jests documentation](https://jestjs.io/docs/api#describename-fn). Basically, a `describe` bundles up multiple test cases for better readability. 

```ts
// example.spec.ts
describe('MyPlugin Tests', () => {

});
```

3. To the describe, add a test case. Please note that `it` and `test` are aliases, so you can also call `test`, depending on your preference. Read more in [Jests documentation](https://jestjs.io/docs/api#testname-fn-timeout)

```ts
// example.spec.ts
describe('MyPlugin Tests', () => {

  it('should be able to execute test', () => {
    expect("hello").toBeTruthy();
  });
});

// this is necessary to conform the isolatedModules compiler option and can be removed as soon as an import is added
export {};
```

4. To execute the test, open a terminal and execute `npm run test`. This triggers the script you've added to package.json and should execute Jest, showing you a successful test run. 

### Testing plugin code

The previous test case made sure that Jest is correctly integrated to the project. In general, testing a string literal does not hold much value. The goal of automated testing is to run code and ensure that it meets certain expectations. In our case, we want to test plugin related code.

Unfortunately, Obsidian API is not straight forward to test. Obsidian functionality is only available if the code runs in context of an Obsidian app and will not be available when running code in our testing environment. The `obsidian` node module contains types only. This means Jest will fail to find and execute i.e. classes and functions. It will work fine for types.

First of all, exchange the static test case from before with one using the plugin class. Replace your test file content with:

```ts
// example.spec.ts
import MyPlugin from "./main";

describe("MyPlugin Tests", () => {

  it("should be importable", () => {
    expect(MyPlugin).toBeTruthy();
  });
});
```

Run `npm run test`. It'll fail with an `Cannot find module 'obsidian' from 'main.ts'` error due to the reasons explained above. 

> [!info] Obsidian API usage in other files
> Please note that the file under test does not need to use the Obsidian API directly to encounter this error. You'll also run into it if an import in your file under tests refers the Obsidian API or an import of an imported file, etc.

There are multiple ways working around this error and this guide will detail two of them. They're not exclusive. Depending on the scope of your plugin it might be worthwhile to combine both approaches. 

#### Mocking Obsidian API 

Jest carries functionality to mock a variety of things, including dependencies. In case of the Obsidian API, a [manual ES6 class mock](https://jestjs.io/docs/es6-class-mocks#manual-mock) is required.

Mocking the Obsidian API does not lessen the usefulness of your tests. When testing, you will need to assume that any third party dependency, including the Obsidian API, is working like expected and concentrate on testing only code under your own responsibility, since this is the only code you can fix. 

1. Create a folder named `__mocks__` at the root of your plugin folder
2. In `__mocks__`, create a file called `obsidian.ts` and provide an empty (mock) class for every import listed at the top of `main.ts`:

```ts
// obsidian.ts
export class Modal {}
export class Notice {}
export class Plugin {}
export class PluginSettingTab {}
export class Setting {}

// mocking these classes is not necessary. They're part of the import but only accessed as types, which should work out of the box.
// export class App {}
// export class MarkdownView {}
// export class Editor {}
```
3. Run `npm run test` again and your test should succeed. 

This mock is only enough to enable Jest to read `main.ts` at all. It is insufficient for other scenarios. 
For example, add a second test case below the existing one:

```ts
// example.spec.ts
// [... describe and first test case ...]
it('onload should load default settings', async () => {
  const plugin = new MyPlugin({} as any, {} as any);
  await plugin.onload();

  expect(plugin.settings).toEqual({
    mySetting: 'default'
  });
});
```

Run it with `npm run test`. It'll fail due to a `TypeError: this.loadData is not a function` error.
`loadData` is provided by the `Plugin` class `MyPlugin` is extending from, but our mock is an empty class and not providing such a function. To have the `onload()` function running successfully, we need to provide mocks for every accessed function from the Obsidian API. Enhance `__mocks__/obsidian.ts` like follows:

```ts
// obsidian.ts
export class Modal {}
export class Notice {}
export class Plugin {
  loadData() {}
  saveData() {}
  addRibbonIcon() {
    return {
      addClass: () => {}
    };
  }
  addStatusBarItem() {
    return {
      setText: () => {}
    };
  }
  addCommand() {}
  addSettingTab() {}
  registerDomEvent() {}
  registerInterval() {}
}
export class PluginSettingTab {}
export class Setting {}

// mocking these classes is not necessary. They're part of the import but only accessed as types, which should work out of the box.
// export class App {}
// export class MarkdownView {}
// export class Editor {}
```

> [!attention] Enhancing mocks when necessary
> For every new element you access from the Obsidian API, except for types, you'll need to enhance `__mocks__/obsidian.ts` with appropiate mocks to test your code. 

This will provide mocks for all functions that are called in `onload()`. Run `npm run test` again - your test will unfortunately still fail.

##### Use jsdom to enable usage of browser specific API 

With the Obsidian mock in place, your test will still fail, because the example plugin accesses `document` and `window` in `onload()`. This fails since Jest is by default running in a `node` test environment that does not provide such objects. The most straight forward way to fix this is to switch to the jsdom test environment that emulates the capabilities of a browser (or electron app).

1. Open a terminal, navigate to your plugins root folder and run `npm i jest-environment-jsdom`
2. In `jest.config.js` adjust `testEnvironment` to use `jsdom`: `testEnvironment: "jsdom",`
3. Run the test via `npm run test`. Both test cases should be green.

#### Extract business logic while keeping Obsidian API usage

You can avoid or limit mocking `obsidian` by loosening the dependency of the code to test from Obsidian API usages. 

As detailed in the first approach, you'll be only interested in testing your own code and need to assume that third party code, including the Obsidian API, is doing its job. This opens up the opportunity to extract any business logic you're doing in a separate file and put this file under test instead of `main.ts`.

Lets assume you want to test following code of `main.ts` (line 19 to 38): 

```ts
// main.ts
// This creates an icon in the left ribbon.
const ribbonIconEl = this.addRibbonIcon('dice', 'Sample Plugin', (evt: MouseEvent) => {
  // Called when the user clicks the icon.
  new Notice('This is a notice!');
});
```

To make this piece of code testable without depending on the Obsidian API, we need to cut out custom logic from the rest. In this example, it's the callback function of `addRibbonIcon`. 

> [!hint] Structuring with folders
> For reason of simplicity, this guide adds files to the root folder. Generally, it is a good idea to structure your code in folders, i.e. productive code in `src` and tests in `tests` to keep your code base better maintainable. 

1. Create a new file `myplugin.ts` in your projects root folder and add a default exported class to it:

```ts
// myplugin.ts
export default class MyPluginLogic {

}
```

2. Extract the callback of `addRibbonIcon` to a function (see [[How to test plugin code that uses Obsidian APIs#Move logic out to separate files]] for more infos how to extract code)

```ts
// myplugin.ts
export default class MyPluginLogic {
  static ribbonIconCallback() {
    // Called when the user clicks the icon.
    new Notice('This is a notice!');
  }
}
```

This still carries a call to the Obsidian API (to `Notice`) that needs to be extracted. To not depend on the Obsidian API in our custom file, we'll instead pass the dependency in from our calling context (which will be `main.ts`). 

3. Pass in Obsidian API depending functionality as function parameter. Please note that `any` is not a good choice for a type - we'll take a look at this problem in [[How to add automated tests to your plugin#Using Obsidian API for typing in extracted business logic|Using Obsidian API for typing in extracted business logic]].

```ts
// myplugin.ts
export default class MyPluginLogic {
  static ribbonIconCallback(notice: any) {
    // Called when the user clicks the icon.
    new notice('This is a notice!');
  }
}
```

4. Adjust the callback in `main.ts` to use the extracted function

```ts
// main.ts
import MyPluginLogic from "./myplugin";

// [other code ...]
const ribbonIconEl = this.addRibbonIcon('dice', 'Sample Plugin', (evt: MouseEvent) => {
  MyPluginLogic.ribbonIconCallback(Notice);
});
```

Restart Obsidian to check manually that the ribbon icon is still showing you the notice when clicked.

> [!attention] Correct import path
> It might happen that Visual Studio Code auto-imports `MyPluginLogic` like this:
> ```ts
> import MyPluginLogic from "myplugin";
> ```
> Mind the missing `./` in front of the file name. If your code is not working, try adjusting the import to `import MyPluginLogic from "./myplugin";`  

Having the business logic extracted, it's now possible to test `myplugin.ts` instead of `main.ts` and avoid mocking `obsidian`. 

5. Remove or comment out `__mocks__/obsidian.ts` to make sure the following works without any mocks. 
6. Replace the content of `example.spec.ts` with:

```ts
// example.spec.ts
import MyPluginLogic from "./myplugin";

describe("MyPlugin Tests", () => {
  it('should create a notice with This is a notice! as text', () => {
    const mockNotice = jest.fn();
    MyPluginLogic.ribbonIconCallback(mockNotice);

    expect(mockNotice).toHaveBeenCalledWith("This is a notice!");
  });
});
```

6. Run the test via `npm run test`. It should be green.

Mind that you will not be able to test if you really registered a corresponding ribbon icon with this approach. Generally, separating business logic from the logic that's necessary to integrate with Obsidian can help with readability and maintainability and might be valuable not only for testing. 

##### Using Obsidian API for typing in extracted business logic

As previously mentioned, using types of the Obsidian API is not a problem per se. To leverage the power of typescript and use the correct types, we can enhance `myplugin.ts` to correctly type the dependency the callback expects, even if this means having an `obsidian` import inside the code. 

Since we're using a constructor here, you cannot just type the parameter as `notice: Notice`. This would expect a already constructed Notice object; instead, use an [abstract construct signature](https://www.typescriptlang.org/docs/handbook/2/classes.html#abstract-construct-signatures).

```ts
// myplugin.ts
import { Notice } from "obsidian";

export default class MyPluginLogic {
  static ribbonIconCallback(notice: new (msg: string) => Notice) {
    // Called when the user clicks the icon.
    new notice('This is a notice!');
  }
}
```

Run your test via `npm run test`. It should still be green, without any mock in place. 

#### Extract business logic and abstract from Obsidian API usage

The previous example does not appear too useful since we extracted business logic that only called, again, an Obsidian API function. The example plugin is designed to showcase usage of Obsidian API and thus makes heavily use of it, which makes it unsuited for an example for extracting pure business logic. To showcase this, it is necessary to first enhance the example plugin with some more functionality. Replace line 14 to 23 of `main.ts` with following:

```ts
// main.ts

// [...imports, const, interfaces...]
export default class MyPlugin extends Plugin {
  settings: MyPluginSettings;
  data: {
    numberOfRolls: number;
    username: string;
    limit?: number;
  }

  async onload() {
    await this.loadSettings();
    // mocking some data for showcasing purposes
    this.data = {
      numberOfRolls: 3,
      username: 'Alice',
      limit: 6
    };

    // This creates an icon in the left ribbon.
    const ribbonIconEl = this.addRibbonIcon('dice', 'Sample Plugin', (evt: MouseEvent) => {
      // Called when the user clicks the icon.
      let message;
      if (this.data.limit && this.data.limit <= this.data.numberOfRolls) {
        message = "Oh no, you've surpassed your daily limit!";
      } else {
        const diceRoll = Math.floor(Math.random() * 7);
        this.data.numberOfRolls++;

        message = `Hey, ${this.data.username}! You've rolled a ${diceRoll} - this was your ${this.data.numberOfRolls} roll today.`;

        if (this.data.limit && this.data.numberOfRolls >= (this.data.limit - 2)) {
          message += ` Watch out! You only have ${this.data.limit - this.data.numberOfRolls} rolls left today!`;
        } 
      }

      new Notice(message);
    });
    // [... rest of the code]
```

This will return you a virtual dice roll number as long as you stay under the configured limit. None of this code depends directly on Obsidian and makes it a good candidate to extract it to a separate function in a separate file. Replace the content of `myplugin.ts` with following code:

```ts
// myplugin.ts
export default class MyPluginLogic {
  static generateDiceRollMessage(data: any): string {
    let message;
    if (data.limit && data.limit <= data.numberOfRolls) {
      message = "Oh no, you've surpassed your daily limit!";
    } else {
      const diceRoll = Math.floor(Math.random() * 7);
      data.numberOfRolls++;

      message = `Hey, ${data.username}! You've rolled a ${diceRoll} - this was your ${data.numberOfRolls} roll today.`;

      if (data.limit && data.numberOfRolls >= (data.limit - 2)) {
        message += ` Watch out! You only have ${data.limit - data.numberOfRolls} rolls left today!`;
      }
    }
  
    return message;
  }
}
```

> [!info] Any typing is bad typing
> Instead of `any`, you'd provide an interface - in a third file - that describes your data structure and use it here as a type, like the already existing `MyPluginSettings`. Due to simplicity, we'll leave that out here.

Since `data` is fetched (normally) by a Obsidian API call, we'll fetch it beforehand and pass it to the function. This will require a small refactor, since you'll need to remove `this.` before `data`. Showing the Notice will stay outside of the extracted function too, to not have any dependency on Obsidian API. 
All that's left is to use the extracted function in `main.ts`:

```js
// main.ts
const ribbonIconEl = this.addRibbonIcon('dice', 'Sample Plugin', (evt: MouseEvent) => {
  // Called when the user clicks the icon.
  const message = MyPluginLogic.generateDiceRollMessage(this.data);
  new Notice(message);
});
```

It's possible to test the extracted code by i.e. making sure that the limit is respected without providing any mock for `obsidian`.

```ts
// example.spec.ts
import MyPluginLogic from "./myplugin";

describe("MyPlugin Tests", () => {
  it('should display a static message if the configured limit is exceeded', () => {
    const mockData = {
      username: "Bob",
      numberOfRolls: 10,
      limit: 8
    };

    const message = MyPluginLogic.generateDiceRollMessage(mockData);

    expect(message).toEqual("Oh no, you've surpassed your daily limit!");
  });
});
```

This does not test if the notice is really shown, but enables you to test your custom logic that builds the message without the need of potentially complex mocks. You could opt in to manage showing the notice in your extracted function, as well, like shown in the previous example. How you split your code and which parts you want to put under test can be a difficult question to answer and depends on the individual code you're writing, its complexity, and its importance. As mentioned before, combining the presented approaches to test all relevant parts of your plugin is a valid way to go.

## Closing words

While setting up tests might appear tedious at times and is a skill to learn, with a growing code base and growing complexity automated tests can be an enormous help and sometimes the only way to make sure that nothing is seriously broken. It'll give you the confidence to do refactors to your code without the need of extensive manual tests and will also encourage a cleaner structure of productive code for the sake of test-ability.


%% Hub footer: Please don't edit anything below this line %%

# This note in GitHub

<span class="git-footer">[Edit In GitHub](https://github.dev/obsidian-community/obsidian-hub/blob/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20add%20automated%20tests%20to%20your%20plugin.md "git-hub-edit-note") | [Copy this note](https://raw.githubusercontent.com/obsidian-community/obsidian-hub/main/04%20-%20Guides%2C%20Workflows%2C%20%26%20Courses/Guides/How%20to%20add%20automated%20tests%20to%20your%20plugin.md "git-hub-copy-note") | [Download this vault](https://github.com/obsidian-community/obsidian-hub/archive/refs/heads/main.zip "git-hub-download-vault") </span>
