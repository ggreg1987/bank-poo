
class Extract:
    def __int__(self, extract: list):
        self.__extract = extract

    def add_extract(self, value):
        self.__extract.append(value)

    def extract_list(self):
        for ex in self.__extract:
            print(ex)

