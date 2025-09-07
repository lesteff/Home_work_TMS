with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("123 ааа456 1x2y3z 4 5 6")

with open('file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

content_sum = 0
current_number = ''

for char in content:
    if char.isdigit():
        current_number += char
    else:
        if current_number:
            content_sum += int(current_number)
            current_number = ''
if current_number:
    content_sum += int(current_number)

print(f"Сумма {content_sum}")