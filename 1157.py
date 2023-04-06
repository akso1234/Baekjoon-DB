from collections import Counter

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

word = input()
word = list(word.upper())
ex_list = modefinder(word)

if len(ex_list) >= 2:
    print("?")
else:
    print(ex_list[0])