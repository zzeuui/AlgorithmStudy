import sys
input = sys.stdin.readline

def check_bracket(sentence):
    stack = list()
    for s in sentence:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False

    return True

if __name__=='__main__':
    for _ in range(int(input().rstrip())):
        sentence = list(input().rstrip())
        
        if check_bracket(sentence):
            print("YES")
        else:
            print("NO")
