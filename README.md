# LanguageManager (In development)
 An open source Python module for translating your app in many languages.
## How to add LanguageManager in your app?
 Just follow these steps:
 * Copy the file "language_manager.py" in the source root of your project.
 * Create a folder ".language_manager" in the same directory of "language_manager.py".
 * Import language_manager in your app.
###To use Language Manager in your app, just follow these instructions:
 To create a language package, in the .language_manager folder:
 * Call language_manager.LanguageManager.create_language(language_name)

 Create a key (a translation ID with a value):
 * Call language_manager.LanguageManager.create_key(key_name, value, language_package)
 
Delete a key:
 * Call language_manager.LanguageManager.delete_key(key_name, value, language_package)
 
Delete a language package:
 * Call language_manager.LanguageManager.delete_language(language_name, silent=True))
