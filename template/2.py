input_file = "input.txt"
lines = []

with open(input_file) as file:
    values = file.read()
    for line in values.split("\n"):
        lines.append(line)
