seq = list(input())

for i in range(len(seq)):
    if seq[i] != ' ' and seq[i].isalpha():
        if 'A' <= seq[i] <= 'Z':
            ind = (ord(seq[i])+13)%(ord('Z')+1)
            if ind < ord('A'):
                ind += ord('A')

        elif 'a' <= seq[i] <= 'z':
            ind = (ord(seq[i])+13) % (ord('z')+1)
            if ind < ord('a'):
                ind += ord('a')

        seq[i] = chr(ind)

print(''.join(seq))
