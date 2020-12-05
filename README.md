# LanguageManager
 An open source Python module for translating your app in many languages.
## How to add LanguageManager in your app?
 Just follow these steps:
 * Copy the source files somewhere in your project
 * Add a folder called `packages` in the directory `language_manager`
 * Add a file in this folder named, for example `en-US.langpkg`.
 * In this file, add your keys and values, like in a Python dictionary:
   
`LANGUAGE = {` The root of the dictionary
   
`[TAB]"name": "en-US",` The name of the language
    
`[TAB]"contents": {` The sub-dictionary in which you will put your keys

`[TAB][TAB]"main": "Hello World!",` A key called "main" with a value of "Hello World!"

`...`

`[TAB]},`

`}`
### To use Language Manager in your app, just follow these instructions:
 * Import language_manager.LanguageManager in your app (or modules.languagemanager.LanguageManager, for example).
 * To get a key from a language database, call:

`language_manager.LanguageManager.get_key(language_name, key)`