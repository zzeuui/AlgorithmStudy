#must add the two lines below to pass this problem
import sys
input = sys.stdin.readline

if __name__=='__main__':
    stack = list()
    leng = 0
    for _ in range(int(input().rstrip())):
        command = input().rstrip().split()

        if len(command) > 1:
            stack.append(int(command[1]))
            leng += 1
        else:
            command = command[0]
            if command == 'pop':
                if stack:
                    print(stack.pop())
                    leng -= 1
                else:
                    print(-1)
            elif command == 'size':
                print(leng)

            elif command == 'empty':
                if stack:
                    print(0)
                else:
                    print(1)
            elif command == 'top':
                if stack:
                    print(stack[-1])
                else:
                    print(-1)
