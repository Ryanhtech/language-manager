""" Test LanguageManager with this sample. """
import languagemanager

lm_class = languagemanager.LanguageManager()


def run_test():
    print(lm_class.get_key("en-US", "main"))


if __name__ == "__main__":
    run_test()
