a, b = map(int, input().split())
result_list = []
col = 0
row = 0

for i in range(a):
    result_list.append(input())

for i in range(a):
    if 'X' not in result_list[i] :
        row += 1
        
for j in range(b):
    if "X" not in [result_list[i][j] for i in range(a)]:        
        col += 1
print(max(row, col))
