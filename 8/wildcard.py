
def check_word(wild, file_name):

    i = 0
    pos = 0

    #check that wild consist only of '*' and '?'
    check_wild = 1
    for i in list(set(wild)):
        if i != '*' and i != '?':
            check_wild = 0

    if check_wild:
        return True

    while True:
        if wild[i] == file_name[i] or wild[i] == '?':
            pos += 1

        elif wild[i] == '*':

            next_qs = i
            for j in range(i+1, len(wild)):
                if wild[j] == '*' or wild[j] == '?':
                    #if there is a character after '*'
                    if j - next_qs > 1: 
                        next_qs = j
                    else:
                        break;

            #if the next character is '*' or '?'
            #and consist only of '*' and '?'
            if next_qs == i and len(list(set(wild))) == 1:
                return True
            elif next_qs == i:
                return check_word(wild[i+1:], file_name) #pasing

            #string from current wild pattern to the next wild pattern
            mat = ''.join(wild[i+1:j])

            #check if a matching the string exists in the file name
            try: ind = ''.join(file_name).index(mat)
            except: ind = -1

            if ind != -1:
                pos += ind
                return check_word(wild[i+1:], file_name[ind:]) #pasing
            else:
                return False
        
        i += 1
        if i == len(wild) or i == len(file_name):
            break

    if pos == len(file_name): #length of file name and pos is same
        return True
    else:
        return False


if __name__=='__main__':
    case_n = int(input())

    for _ in range(case_n):
        wild = list(input())

        n = int(input())
        for _ in range(n):
            file_name = list(input())
            print(check_word(wild, file_name))
