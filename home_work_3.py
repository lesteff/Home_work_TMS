input_file = open('input.txt', 'r', encoding='utf-8')
output_file = open('output.txt', 'w', encoding='utf-8')


line_number = 1
for line in input_file:
    words = line.split()

    if words:

        counter = {}
        for word in words:

            clean_word = word.lower().strip('.,!?')
            if clean_word:
                counter[clean_word] = counter.get(clean_word, 0) + 1


        most_common_word = max(counter, key=counter.get)
        output_file.write(f"Строка {line_number}: {most_common_word} - {counter[most_common_word]}\n")

    line_number += 1


input_file.close()
output_file.close()