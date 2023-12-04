from pprint import pprint

input_file = "input.txt"
lines = []

with open(input_file) as file:
    values = file.read()
    for line in values.split("\n"):
        lines.append(line)

pool = lines


class Card:
    __winning_set = []
    __player_set = []

    __matching_set = []

    __card_value = None
    __card_number = None

    def __init__(self, text: str):
        text = text.split('|')
        card_number_and_winning_set = text[0]
        current_player_set = text[1]

        self.__card_number = int(card_number_and_winning_set.split(": ")[0].replace("Card ", ""))

        self.__player_set = [int(value) for value in current_player_set.strip().replace("  ", " ").split(" ")]
        self.__winning_set = [int(value) for value in
                              card_number_and_winning_set.split(": ")[1].strip().replace("  ", " ").split(" ")]

        self.__matching_set = [value for value in self.__player_set if value in self.__winning_set]

        self.__card_value = 2 ** (len(self.__matching_set) - 1) if len(self.__matching_set) > 0 else 0

    def __str__(self):
        return f"Card no. {self.__card_number}, winning set : [{', '.join([str(value) for value in self.__winning_set])}], player set : [{', '.join([str(value) for value in self.__player_set])}], matching set : [{', '.join([str(value) for value in self.__matching_set])}] of value {self.__card_value}"

    def getNumber(self):
        return self.__card_number

    def getValue(self):
        return self.__card_value


somme = 0

for line in pool:
    card = Card(line)
    print(card)
    somme += card.getValue()

print(somme)
