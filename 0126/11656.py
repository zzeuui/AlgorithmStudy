seq = input()
temp = list()
for i in range(len(seq)):
    temp.append(seq[i:])

temp = sorted(temp)
print('\n'.join(temp).rstrip())
