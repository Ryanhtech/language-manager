# LanguageManager
 An open source Python module for translating your Python apps in many languages. **This software is outdated, and this repository is no longer maintained (it might contain outdated links)! You can still use it, but at your own risks. It will be replaced by a new project on GitHub soon (~may/june).**
## How to add LanguageManager in your app?
 Just follow these steps:
 * Copy the source files somewhere in your project (*It is recommended to create a new directory in your project just for LanguageManager*)
 * Add a file in the folder `language_manager/packages`, for example `en-US.langpkg`.
 * In this file, add your keys and values, like in a Python dictionary:
   
`LANGUAGE = {` The root of the dictionary
   
`[TAB]"name": "en-US",` The name of the language
    
`[TAB]"contents": {` The sub-dictionary in which you will put your keys

`[TAB][TAB]"main": "Hello World!",` A key called "main" with a value of "Hello World!"

`[TAB][TAB]...` Other keys and values

`[TAB]},`

`}`
### To use Language Manager in your app, just follow these instructions:
 * Import language_manager.LanguageManager in your app (or modules.languagemanager.LanguageManager, for example).
 * To get a key from a language database, call:

`language_manager.LanguageManager.get_key(language_name, key)`
