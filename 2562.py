ex_list = []
for i in range(9):
    example = int(input())
    ex_list.append(example)

print(max(ex_list))
print(ex_list.index(max(ex_list)) + 1)