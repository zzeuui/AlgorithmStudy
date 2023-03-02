# 정석 c++: https://damper.tistory.com/37
"""
#파이썬과 같이 배열로 푼 c++ 답
#include <iostream>

#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int nCases;
    cin >> nCases;

    while (nCases--) {
        int n;
        cin >> n;
        deque<int> seq(n);
        for (int i = 0; i < n; i++) 
            seq[i] = i;
        for (int i = 0; i < n; i++) {
            int moves;
            cin >> moves;
            auto it = seq.begin() + i;
            seq.insert(it - moves, seq[i]);
            seq.erase(seq.begin() + i + 1);
        }
        int *arr = new int[n];
        for (int i = 0; i < n; i++) 
            arr[seq[i]] = i+1;
        
        cout << arr[0];
        for (int i = 1; i<n; i++)
            cout << " " << arr[i];
        cout << '\n';
        
    }
    return 0;
}
"""
import sys
input = sys.stdin.readline

if __name__=='__main__':

    for _ in range(int(input())):
        N = int(input())
        A = tuple(map(int, input().split()))
        B = [ n for n in range(1, N+1)]
        C = [0] * N

        for i in range(N-1, -1, -1):
            t = B[i-A[i]] #남은 숫자들중 A[i]만큼 큰 수를 가진 값
            C[i] = t 
            B.pop(i-A[i]) #제외

        for i in range(N):
            print(C[i], end=" ")

        print("")
