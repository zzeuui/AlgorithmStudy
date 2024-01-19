import sys
input = sys.stdin.readline

if __name__=='__main__':
    sequence = list(input().rstrip())
    cur = len(sequence)
    for _ in range(int(input().rstrip())):
        command = input().rstrip().split()

        if len(command) > 1:
            c, i = command
            sequence.append('')
            sequence[cur+1:] = sequence[cur:]
            sequence[cur] = i
            cur += 1
        else:
            c = command[0]

            if (c == 'L' or c == 'B') and cur > 0:
                if c == 'B':
                    sequence[cur-1:] = sequence[cur:]
                cur -= 1
            elif c == 'D' and cur <= len(sequence):
                cur += 1

    print(''.join(sequence))
