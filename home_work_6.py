def codeVigenere(text, key, mode='encrypt'):

    result = ''
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'decrypt':
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


print("Шифр Виженера")
print("1 - Шифровать")
print("2 - Расшифровать")
choice = input("Выберите: ")
text = input("Сообщение: ")
key = input("Ключ (слово): ")

if choice == '1':
    encrypted = codeVigenere(text, key, 'encrypt')
    print("Зашифровано:", encrypted)
elif choice == '2':
    decrypted = codeVigenere(text, key, 'decrypt')
    print("Расшифровано:", decrypted)
else:
    print("Ошибка!")