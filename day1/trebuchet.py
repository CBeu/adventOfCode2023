import re

class adventReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.loadedData = []

    def read(self):
        with open(self.filepath, "r") as file:
            for line in file:
                self.loadedData.append(line.strip())
        return self.loadedData

class trebuchet:
    def __init__(self, filepath):
        self.filepath = filepath
        self.reader = adventReader(self.filepath)
        self.loadedData = self.reader.read()
    
    def sum(self):
        digits = [re.findall("\d", x) for x in self.loadedData]
        return sum([int(x[0] + x[-1]) for x in digits])
    
    def spelledOut(self):
        str2num = {"one": "o1n", "two": "t2o", "three": "th3ee", "four": "f4ur", "five": "f5ve", "six": "s6x", "seven": "s7ven", "eight": "e8ght", "nine": "n9ne"}
        for i in range(len(self.loadedData)):
            spelled = self.loadedData[i]
            for key in str2num.keys():
                spelled = spelled.replace(key, str2num[key])
            self.loadedData[i] = spelled

            

#Sample
x = trebuchet("day1/sample.txt")
print((x.sum()) ==142)

#Part 1
y = trebuchet("day1/input.txt")
print((y.sum()))

#Part 2 Sample
z = trebuchet("day1/part2sample.txt")
z.spelledOut()
print((z.sum()) == 281)

#Part 2
z = trebuchet("day1/input.txt")
z.spelledOut()
print((z.sum()))