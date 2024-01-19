import sys
input = sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input().rstrip())):
        sentence = input().rstrip().split()
        sentence = [s[::-1] for s in sentence]
        print(' '.join(sentence))
