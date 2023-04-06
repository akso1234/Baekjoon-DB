first = int(input())
second = int(input())
third = int(input())

result = first * second * third
result = list(str(result))
result = list(map(int, result))

for i in range(0, 10):
    print(result.count(i))