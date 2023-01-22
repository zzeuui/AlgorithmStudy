import itertools

if __name__=='__main__':
    case_n = int(input())
    
    for _ in range(case_n):
        n_l = list(map(int, input().split()))
        cost = list(map(int, input().split()))

        min_cost = sum(cost)/len(cost)
        for i in range(n_l[1], len(cost)+1):
            e = i
            for j in range(len(cost)-e+1):
                tot_cost = sum(cost[j:i])/e
                if tot_cost < min_cost:
                    min_cost = tot_cost

                i += 1

        print(min_cost)
