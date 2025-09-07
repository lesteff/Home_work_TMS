with open('stop_words.txt', 'r', encoding='utf-8') as stop_file:
    stop_words = stop_file.read().split()


filename = ("text.txt")


with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()


for word in stop_words:

    start = 0
    while True:

        pos = text.lower().find(word.lower(), start)
        if pos == -1:
            break


        original_word = text[pos:pos + len(word)]
        stars = '*' * len(original_word)
        text = text[:pos] + stars + text[pos + len(word):]
        start = pos + len(stars)


print(text)