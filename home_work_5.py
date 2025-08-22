def codeCeasar(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result



print("1 - Шифровать")
print("2 - Расшифровать")
choice = input("Выберите: ")
text = input("Сообщение: ")

shift = 3  # сдвиг

if choice == '1':
    print("Зашифровано:", codeCeasar(text, shift))
elif choice == '2':
    print("Расшифровано:", codeCeasar(text, shift, 'decrypt'))
else:
    print("Ошибка!")