x, y = input().split()

x = list(x)
y = list(y)

while True:
    if int(x[len(x) - 1]) == 0:
        del x[len(x) - 1]
    else:
        break

while True:
    if int(y[len(y) - 1]) == 0:
        del y[len(y) - 1]
    else:
        break

x.reverse()
y.reverse()

x = ''.join(x)
y = ''.join(y)

result = str(int(x) + int(y))
result = list(result)
result.reverse()
result = ''.join(result)

print(int(result))
