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
    def get_key(self, language_name, key):
        package_path = f"language_manager/packages/{language_name}.langpkg"
        with open(package_path, "r") as file:
            with open(f"temp.py", "w") as temp_file:
                self.__log__(f"--- Call to LanguageManager.get_key(self, {language_name}, {key}) ---\n"
                             f"Copying file {package_path} to LanguageManager root/temp.py\n")
                temp_file.write(file.read())
                self.__log__("done.\n")

        import temp
        self.__log__(f"Getting key \"{key}\"\n")
        return_val = temp.LANGUAGE["contents"][key]
        self.__log__("Done.")
        del temp
        self.__log__("\n--- Finished function call ---\n\n")
        return return_val

    def clean(self):
        os.remove("temp.py")

    def __log__(self, val):
        if lm_settings["debug"]:
            try:
                log_file = open("language_manager/info/language_manager.log", "a")
            except FileNotFoundError:
                log_file = open(lm_settings["logfile"], "w")
            log_file.write(val)
            log_file.close()
