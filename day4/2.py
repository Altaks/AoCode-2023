from pprint import pprint

input_file = "input.txt"
lines = []

with open(input_file) as file:
    values = file.read()
    for line in values.split("\n"):
        lines.append(line)

pool = lines


class Card:
    pass

class Card:
    __winning_set = []
    __player_set = []

    __matching_set = []
    __matching_amount = None
    __matching_set_instances: list[Card] = []

    __card_number = None

    def __init__(self, text: str):
        text = text.split('|')
        card_number_and_winning_set = text[0]
        current_player_set = text[1]

        self.__card_number = int(card_number_and_winning_set.split(": ")[0].replace("Card ", ""))

        self.__player_set = [int(value) for value in current_player_set.strip().replace("  ", " ").split(" ")]
        self.__winning_set = [int(value) for value in
                              card_number_and_winning_set.split(": ")[1].strip().replace("  ", " ").split(" ")]

        self.__matching_amount = len([value for value in self.__player_set if value in self.__winning_set])

        self.__matching_set = [self.__card_number + number for number in range(1, self.__matching_amount+1)]
    def __str__(self):
        return (f"Card no. {self.__card_number}, \n"
                f"Winning set : [{', '.join([str(value) for value in self.__winning_set])}], \n"
                f"Player set : [{', '.join([str(value) for value in self.__player_set])}], \n"
                f"Matching amount : {self.__matching_amount}\n"
                f"Matching set : [{', '.join([str(value) for value in self.__matching_set])}]\n"
                f"Matching set instances : [{', '.join([str(card.getNumber()) for card in self.__matching_set_instances])}]")

    def getNumber(self):
        return self.__card_number

    def countTotalCopies(self):
        return 1 + sum([card.countTotalCopies() for card in self.__matching_set_instances])

    def queryMatchingSetInstances(self, instances: dict):
        self.__matching_set_instances = [instances[number] for number in self.__matching_set]


card_instances = dict()
somme = 0

for line in pool:
    card = Card(line)
    card_instances[card.getNumber()] = card

for card_number, card in card_instances.items():
    card.queryMatchingSetInstances(card_instances)

for card_number, card in card_instances.items():
    somme += card.countTotalCopies()

print(somme)