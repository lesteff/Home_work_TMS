filename = 'children.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.readlines()

for children in text:
    parts = children.split()
    surname = parts[0]
    name = parts[1]
    grade = int(parts[2])

    if grade < 3:
        print(f"{surname} {name} оценка {grade}")
        