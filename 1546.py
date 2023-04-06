new_list = []
result = 0

n = int(input())
num_list = list(map(int, input().split()))

max_num = max(num_list)
for i in range(0, n):
    new_list.append(num_list[i] / max_num * 100)

for j in range(0, n):
    result = result + new_list[j]

print(result / n)