a, b = map(int, input().split())

mini = min(a, b)
while True:
    if a%mini == 0 and b%mini == 0:
        break

    mini -= 1
print(mini)

maxi = max(a, b)
i = 1
while True:
    if (maxi*i)%a == 0 and (maxi*i)%b == 0:
        maxi *= i
        break
    i += 1

print(maxi)
