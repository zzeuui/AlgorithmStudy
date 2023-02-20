from random import uniform

if __name__=='__main__':
    case_n = input()

    for _ in range(int(case_n)):
        members = list(map(int, list(input().replace('F', '1').replace('M', '0'))))
        fans = list(map(int, list(input().replace('F', '1').replace('M', '0'))))

        """
        members = list()
        fans = list()
        for _ in range(20):
            num = uniform(0.0, 1.0)

            if num > 0.8:
                members.append(1)
            else:
                members.append(0)

        for _ in range(200000):
            fans.append(1)
        """

        n_members = len(members)

        hug = 0
        for i in range(len(fans)-n_members+1):
            cur_fan = fans[i:i+n_members]

            if sum([1 for (m, c_f) in zip(members, cur_fan) if m+c_f > 0]) == n_members:
                hug += 1

        print(hug)
