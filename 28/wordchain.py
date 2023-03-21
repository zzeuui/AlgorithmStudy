# -*- coding: utf-8 -*- 
import sys

alphabets = "abcdefghijklmnopqrstuvwxyz"


def dfs(start, word):
    #graph는 start에 해당하는 알파벳으로 끝나는
    #(단어의 첫글자, 단어전체)의 리스트로 구성됨
    q = graph[start]
    while q:
        next_node, next_word = q.pop()
        dfs(next_node, next_word)

    ans.append(word)

if __name__=='__main__':
    for _ in range(int(input())):
        N = int(input())
        words = []
        for _ in range(N):
            words.append(sys.stdin.readline().rstrip())

        graph = {}
        in_edge = {}
        out_edge = {}
        for al in alphabets:
            graph[al] = []
            in_edge[al] = 0
            out_edge[al] = 0

        for word in words:
            graph[word[-1]].append((word[0], word))
            out_edge[word[-1]] += 1
            in_edge[word[0]] += 1

        #오일러 트레일인지 서킷인지 확인
        #트레일이라면 out_edge와 in_edge가 일치하지 않는 두 점이 존재함
        candidates = []
        for al in alphabets:
            if out_edge[al] != in_edge[al]:
                candidates.append(al)

        ans = []
        #오일러 트레일,
        if len(candidates) == 2:
            start = None
            end = None
            for al in alphabets:
                #오일러 트레일의 시작점
                if in_edge[al] + 1 == out_edge[al]:
                    start = al

                #오일러 트레일의 끝점
                if in_edge[al] == out_edge[al] + 1:
                    end = al
            
            #시작점과 끝점이 존재해야함(None이 아니어야함)
            #그리고 시작 정점이 되는 알파벳부터 탐색 시작
            if start and end:
                dfs(start, "")

        #오일러 서킷,
        #어떤 알파벳에서 시작해도 결과에 영향없음
        elif len(candidates) == 0:
            for al in alphabets:
                #간선이 존재하는 알파벳(정점)에 대해서만
                if in_edge[al] != 0:
                    dfs(al, "")
                    break

        if ans:
            print(" ".join(ans).strip())
        else:
            print("IMPOSSIBLE")
