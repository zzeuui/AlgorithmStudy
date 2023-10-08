import sys
input = sys.stdin.readline

if __name__=='__main__':
    n = int(input())
    schedule = {}
    for i in range(1, n+1):
        t, p = map(int, input().rstrip().split())
        if i+t <= n+1:
            schedule[i] = (t, p)

    net = {k:p for k, (t, p) in schedule.items()}

    if not net:
        print(0)

    else:
        for d, v in schedule.items():
            t, p = v
            for ntd in range(d+t, n+1):
                if ntd in schedule.keys():
                    ntt, ntp = schedule[ntd]
                    net[ntd] = max(net[d]+ntp, net[ntd])

        print(max(net.values()))
