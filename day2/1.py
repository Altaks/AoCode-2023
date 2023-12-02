RED_LIMIT = 12
BLUE_LIMIT = 14
GREEN_LIMIT = 13


class Game:
    __id = None

    __red_count = None
    __blue_count = None
    __green_count = None

    __canBePlayed = True

    def canBePlayed(self):
        return self.__canBePlayed

    def getId(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.__id}, redcount {self.__red_count}, bluecount {self.__blue_count}, greencount {self.__green_count}"

    def __init__(self, description: str):
        description = description.split(": ")
        self.__id = int(description[0].replace("Game ", ""))

        maxes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for value in description[1].replace(";", ",").split(","):
            value_tab = value.strip().split(" ")
            number = int(value_tab[0])
            color = value_tab[1].strip()
            if maxes[color] < number:
                maxes[color] = number

        self.__red_count = maxes["red"]
        self.__blue_count = maxes["blue"]
        self.__green_count = maxes["green"]

        if self.__green_count > GREEN_LIMIT or self.__red_count > RED_LIMIT or self.__blue_count > BLUE_LIMIT:
            self.__canBePlayed = False


input_file = "input.txt"
lines = []

with open(input_file) as file:
    input = file.read()
    for line in input.split("\n"):
        lines.append(line)

somme = 0

for line in lines:
    game = Game(line)
    if game.canBePlayed():
        somme += game.getId()

print(somme)
