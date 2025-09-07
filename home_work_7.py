def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result


with open('input_7.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


encrypted_lines = []
for i, line in enumerate(lines, 1):
    encrypted_line = caesar_cipher(line.strip(), i)
    encrypted_lines.append(encrypted_line)

with open('output_7.txt', 'w', encoding='utf-8') as file:
    for line in encrypted_lines:
        file.write(line + '\n')

print("Зашифрованный текст:")
for line in encrypted_lines:
    print(line)