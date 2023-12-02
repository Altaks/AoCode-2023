class Game:
    __id = None

    __red_count = None
    __blue_count = None
    __green_count = None

    __game_power = 0

    def getGamePower(self):
        return self.__game_power

    def __str__(self):
        return f"ID: {self.__id}, redcount {self.__red_count}, bluecount {self.__blue_count}, greencount {self.__green_count}"

    def __init__(self, line: str):
        line = line.split(": ")
        self.__id = int(line[0].replace("Game ", ""))

        maxes = {
            "red": 0,
            "green": 0, 
            "blue": 0,
        }

        for value in line[1].replace(";", ",").split(","):
            value_tab = value.strip().split(" ")
            number = int(value_tab[0])
            color = value_tab[1].strip()
            if maxes[color] < number:
                maxes[color] = number

        self.__red_count = maxes["red"]
        self.__blue_count = maxes["blue"]
        self.__green_count = maxes["green"]

        self.__game_power = self.__red_count * self.__blue_count * self.__green_count


input_file = "input.txt"
lines = []

with open(input_file) as file:
    values = file.read()
    for line in values.split("\n"):
        lines.append(line)

somme = 0

for line in lines:
    somme += Game(line).getGamePower()

print(somme)
