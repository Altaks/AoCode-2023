input_file = "input.txt"
lines = []

with open(input_file) as file:
    values = file.read()
    for line in values.split("\n"):
        lines.append(line)


class NumberRectangle:
    __left_up = (None, None)
    __right_down = (None, None)
    __value = None

    def __init__(self, left: int, right: int, line: int, text: str):
        self.__left_up = (left, line)
        self.__right_down = (right, line)

        # get value from text
        self.__value = int(text[left:right + 1])

    def getLeft(self):
        return self.__left_up[0]

    def getRight(self):
        return self.__right_down[0]

    def getLine(self):
        return self.__left_up[1]

    def getUp(self):
        return self.__left_up[1]

    def getDown(self):
        return self.__right_down[1]

    def getValue(self):
        return self.__value

    def __str__(self):
        return f"Valeur: {self.__value},  minX:{self.minX()}, minY:{self.minY()}, maxX: {self.maxX()}, maxY: {self.maxY()}"

    def minX(self) -> int:
        return self.__left_up[0]

    def maxX(self) -> int:
        return self.__right_down[0]

    def minY(self) -> int:
        return self.__left_up[1]

    def maxY(self) -> int:
        return self.__right_down[1]


class SymbolRectangle:
    __left_up = (None, None)
    __right_down = (None, None)
    __symbol = None

    def __init__(self, left: int, right: int, up: int, down: int, symbol: str):
        self.__left_up = (left, up)
        self.__right_down = (right, down)

        self.__symbol = symbol

    def getLeft(self):
        return self.__left_up[0]

    def getRight(self):
        return self.__right_down[0]

    def getUp(self):
        return self.__left_up[1]

    def getDown(self):
        return self.__right_down[1]

    def getSymbol(self):
        return self.__symbol

    def __str__(self):
        return f"Symbol: {self.__symbol} minX:{self.minX()}, minY:{self.minY()}, maxX: {self.maxX()}, maxY: {self.maxY()}"

    def minX(self) -> int:
        return self.__left_up[0]

    def maxX(self) -> int:
        return self.__right_down[0]

    def minY(self) -> int:
        return self.__left_up[1]

    def maxY(self) -> int:
        return self.__right_down[1]

    def intersects(self, rect: NumberRectangle) -> bool:
        return not (
                rect.minX() > self.maxX() or  # trop à droite
                rect.maxX() < self.minX() or  # trop à gauche
                rect.minY() > self.maxY() or  # trop en bas
                rect.maxY() < self.minY()  # trop en haut
        )


pool = lines

numbers_rects = []

# Detect all numbers rectangles
for value in pool:
    line_len = len(value)
    walker_position = 0
    walker_anchor = None

    while walker_position < line_len:
        if value[walker_position].isdigit():

            if not walker_anchor:
                walker_anchor = walker_position

            if walker_position + 1 < line_len and not value[walker_position + 1].isdigit():
                numbers_rects.append(NumberRectangle(walker_anchor, walker_position, pool.index(value), value))
                walker_anchor = None

        walker_position += 1

for nb_rect in numbers_rects:
    print(nb_rect)

print("\n")
symbols_rects = []

# Detect all symbols
for value in pool:
    print(value)

    for i in range(len(value)):
        letter = value[i]
        if not letter.isdigit() and letter != '.':
            # letter is symbol
            symbols_rects.append(
                SymbolRectangle(i - 1, i + 1, pool.index(value) - 1, pool.index(value) + 1, letter)
            )

for symbol_rect in symbols_rects:
    print(symbol_rect)

collides = []

for nb_rect in numbers_rects:
    for symbol_rect in symbols_rects:
        if symbol_rect.intersects(nb_rect):
            collides.append(nb_rect)
            print(f"Detected collision between number {nb_rect.getValue()} and symbol {symbol_rect.getSymbol()}")
            break

somme = 0
for nb in collides:
    somme += nb.getValue()

print(somme)