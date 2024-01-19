#커서를 기준으로 두 스택으로 나눠 담음
#시간 복잡도가 O(1)인 append와 pop 연산으로만 해결 가능함
# st2를 뒤집어 줄 때는 빈 리스트일 경우를 대비해 reversed(list)를 사용한다.

import sys
input = sys.stdin.readline

if __name__=='__main__':
    st1 = list(input().rstrip())
    st2 = list()

    for _ in range(int(input())):
        command = list(input().split())

        if command[0] == 'L':
            if st1:
                st2.append(st1.pop())
        elif command[0] == 'D':
            if st2:
                st1.append(st2.pop())

        elif command[0] == 'B':
            if st1:
                st1.pop()

        else:
            st1.append(command[1])

    st1.extend(reversed(st2))
    print(''.join(st1))
