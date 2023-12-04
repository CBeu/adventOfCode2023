class adventReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, "r") as file:
            for line in file:
                yield line.strip()
