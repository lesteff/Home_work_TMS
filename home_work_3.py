
words = ["sdffd", "gfdgdfgd", "abccba"]
my_list = list(filter(lambda w: w == w[::-1], words))

print(my_list)
