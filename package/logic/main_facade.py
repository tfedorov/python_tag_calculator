from logic import *

class MainFacade:
    def __init__(self):
        self._storage = persistent_storage.PersistenceStorage()

    def synonym_keys(self):
        return [*url_resolver.read_synonyms()]

    def get_command(self, url_or_synonym):
        try:
            valid_url = url_resolver.resolve(url_or_synonym)
            page_content = page_reader.read_content(valid_url)
            custom_logger.log(valid_url)
            tags_num = tags_calculator.calculate(page_content)
            self._storage.save(valid_url, tags_num)
            return tags_num
        except Exception as e:
            msg = "Url error: " + str(e)
            print(msg)
        return msg

    def view_command(self, url_or_synonym):
        try:
            valid_url = url_resolver.resolve(url_or_synonym)
            return self._storage.load(valid_url)
        except Exception as e:
            msg = "Url error: " + str(e)
            print(msg)
        return [msg]
