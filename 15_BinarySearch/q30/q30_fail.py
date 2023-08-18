"""
정확성 정답 45분 (1시간 30분)

정확성 25.0
효율성 30.0

합계 55.0 /100.0

키워드의 접두사와 접미사에만 '?'가 붙는다는 조건에 대해서 처리하면
효율성 테스트 1, 2, 3도 통과하지 않을까?
"""
def binary_search(query, word, start, end):
    if start > end:
        return True
    
    mid = (start+end) // 2
    if query[mid] != word[mid] and query[mid] != '?':
        return False
    
    return binary_search(query, word, start, mid-1) and binary_search(query, word, mid+1, end)

def solution(words, queries):
    answer = [0]*len(queries)
    
    for i, query in enumerate(queries):
        for word in words:
            if len(query) == len(word):
                start = 0
                end = len(query)-1

                if (query[start] == '?' or query[start] == word[start]) and (query[end]=='?' or query[end] == word[end]):
                    if binary_search(query, word, start, end):
                        answer[i] += 1
    
    return answer
