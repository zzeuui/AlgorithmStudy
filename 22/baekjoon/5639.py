import sys
sys.setrecursionlimit(10**9)

def postorder(s, e):
    if s > e:
        return
    mid = e + 1 # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1):
        if nums[s] < nums[i]: #오른쪽 서브트리의 루트 노드
            mid = i
            break

    postorder(s+1, mid-1) #왼쪽 서브트리
    postorder(mid, e) #오른쪽 서브트리                  
    print(nums[s])

    #inorder
    #postorder(s+1, mid-1)               
    #print(nums[s])
    #postorder(mid, e)                  

if __name__=='__main__':

    nums = []
    while True:                            
        try:
            nums.append(int(sys.stdin.readline()))
        except:
            break
        
    postorder(0, len(nums)-1)
