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

class game:
    def __init__(self, gameNum, rounds):
        self.gameNum = gameNum
        # self.rounds is an array of arrays
        self.rounds = rounds
    
    def __str__(self):
        return f"Game {self.gameNum}: {self.rounds}"


class  cubeConundrum:
    def __init__(self, filepath):
        self.reader = adventReader(filepath)
        self.loadedData = self.reader.read()
        self.games = []
        self.validGames = set()
    
    def parse(self):
        for games in self.loadedData:
            gameNumber = int(re.search(r'Game (\d+)', games).group(1))
            gameRounds = []
            rounds = games.split(": ")[1].split(";")
            for round_number, round in enumerate(rounds):
                dic = {}
                parsed = round.replace(" ", "").split(",")
                for item in parsed:
                    match = re.match(r'(\d+)(\D+)', item)
                    dic[match.group(2)] = int(match.group(1))
                gameRounds.append(dic)
            self.games.append(game(gameNumber, gameRounds))
        pass

    def partOne(self, r,g,b):
        for game in self.games:
            if all(r >= round.get("red", 0) and g >= round.get("green", 0) and b >= round.get("blue", 0) for round in game.rounds):
                self.validGames.add(game.gameNum)

    def partTwo(self):
        sum = 0
        for game in self.games:
            maxR, maxG, maxB = 0, 0, 0
            for round in game.rounds:
                maxR = max(maxR, round.get("red", 0))
                maxG = max(maxG, round.get("green", 0))
                maxB = max(maxB, round.get("blue", 0))
            sum += maxR*maxG*maxB
        return sum
    

# Sample
x = cubeConundrum("day2/sample.txt")
x.parse()
x.partOne(12,13,14)
print(sum(x.validGames) == 8)

# Part 1
y = cubeConundrum("day2/input.txt")
y.parse()
y.partOne(12,13,14)
print(sum(y.validGames))

# Part 2
z = cubeConundrum("day2/input.txt")
z.parse()
print(z.partTwo())