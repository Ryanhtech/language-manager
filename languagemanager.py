"""
Copyright 2020, Ryan H.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
from language_manager.info.settings import SETTINGS as lm_settings


class LanguageManager:
    def __init__(self):
        super(LanguageManager, self).__init__()
        self.language_name_global = ""
        self.key_global = ""

    def get_key(self, language_name, key):
        """ Get a key in a language package """
        self.language_name_global = language_name
        self.key_global = key
        package_path = f"language_manager/packages/{language_name}.langpkg"
        if not self.__copy_check_same__(package_path):
            self.__copy__(package_path)

        # Import the temp Python file coming out of the package
        import temp
        self.__log__(f"Getting key \"{key}\"\n")
        # Take the key (type: str)
        return_val = temp.LANGUAGE["contents"][key]
        self.__log__("Done.")
        # Delete the language package from the RAM to free up space
        del temp
        self.__log__("\n--- Finished function call ---\n\n")
        # Return the value of the key
        return return_val

    def clean(self):
        """ Clean the temp files. """
        os.remove("temp.py")  # Delete the file "temp.py", to free up disk space

    def __log__(self, val):
        """ Log ONLY IF the settings value "debug" == True """
        if lm_settings["debug"]:
            try:
                log_file = open("language_manager/info/language_manager.log", "a")
            except FileNotFoundError:
                log_file = open(lm_settings["logfile"], "w")
            log_file.write(val)
            log_file.close()

    def __copy_check_same__(self, file):
        with open(file, "r") as package:
            with open("temp.py", "r") as file:
                if package.read() == file.read():
                    return True
                return False

    def __copy__(self, package):
        with open(package, "r") as file:
            with open(f"temp.py", "w") as temp_file:
                # Log ONLY IF the "debug" value in the settings == True
                self.__log__(f"--- Call to LanguageManager.get_key(self, {self.language_name_global}, "
                             f"{self.key_global}) ---\nCopying file {package} to LanguageManager "
                             f"root/temp.py\n")
                # Copy the language package into the file temp.py in the root of LanguageManager
                temp_file.write(file.read())
                self.__log__("done.\n")
