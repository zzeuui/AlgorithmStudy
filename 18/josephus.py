"""
#timeout

from copy import deepcopy

def kill(people):

    j = 0
    while True:
        temp = deepcopy(people)
        for i, p in enumerate(temp):

            if j == i:
                del people[people.index(p)]
                j += k
                
                if len(people) == 2:
                    people = [str(p+1) for p in people]
                    print(' '.join(people))
                    return

        j = j - len(temp)

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split(' '))
        people = [i for i in range(n)]
        kill(people)
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split(' '))
        people = [i for i in range(1, n+1)]
        j = 0
        while len(people) > 2:
            people.pop(j)
            j = (j + k -1) % len(people)

        print(people[0], people[1])

