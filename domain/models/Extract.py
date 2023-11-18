
class Extract:
    extract: list

    def add_extract(self, value):
        self.extract.append(value)

    def extract(self):
        for ex in self.extract:
            print(ex)

