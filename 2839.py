n = int(input())
count = 0

if n == 4 or n == 7:
    count = -1

else:
    if n % 5 == 0:
        count = int(n / 5)
    elif n % 5 == 1:
        count = int(n / 5) - 1 + 2
    elif n % 5 == 2:
        count = int(n / 5) - 2 + 4
    elif n % 5 == 3:
        count = int(n / 5) + 1
    elif n % 5 == 4:
        count = int(n / 5) - 1 + 3

print(count)



