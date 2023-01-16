
class Picnic():
    def __init__(self, cases_eve):
        self.cases_eve = cases_eve
        self.NUM = 0
        self.cases = list()

    def make_case(self, pairs, students_n, i_j):
        cases = self.cases_eve.copy()

        students_f = [0 for _ in range(students_n)]
        students_f[cases[0]] = 1
        students_f[cases[1]] = 1
        
        i = 0
        for _ in range(int(len(pairs)/2)):
            if students_f[pairs[i]]==0 and students_f[pairs[i+1]]==0:
                cases.append(pairs[i])
                cases.append(pairs[i+1])

                students_f[pairs[i]] = 1
                students_f[pairs[i+1]] = 1

                i_j[0] = i
                i_j[1] = i+1

            i += 2

            if sum(students_f) == students_n:
                break;

        if len(cases) != students_n:
            return
        else:
            self.cases = cases
            self.NUM += 1

        del pairs[i_j[0]]
        del pairs[i_j[0]]

        self.make_case(pairs, students_n, i_j)

        
if __name__ == '__main__':
    case_n = input()

    for _ in range(int(case_n)):
        students_pair = input().split(' ')
        students_n = int(students_pair[0])
        pair_n = int(students_pair[1])

        pairs = input().split(' ')
        pairs = [int(p) for p in pairs]

        cases_eve = [pairs[0], pairs[1]]
        i_j = [-1, -1]
        pairs_c = pairs[2:].copy()

        NUM = 0

        if len(pairs_c) == 0:
            NUM += 1

        else:
            while True:
                while True:
                    picnic = Picnic(cases_eve)

                    if i_j[0] > 0:
                        del pairs_c[i_j[0]]
                        del pairs_c[i_j[0]]
                        i_j = [-1, -1]

                    picnic.make_case(pairs_c, students_n, i_j)

                    NUM += picnic.NUM

                    if len(picnic.cases) == 0:
                        break;
               
                pairs = pairs[2:]
                if len(set(pairs)) != students_n:
                    break;

                cases_eve = [pairs[0], pairs[1]]
                i_j = [-1, -1]
                pairs_c = pairs[2:].copy()

        print(NUM)

