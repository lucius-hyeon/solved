"""
행렬 덧셈

문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

예제 입력 1 
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
예제 출력 1 
4 4 4
6 6 6
5 6 100
"""
## 백준 문제 채점시 런타임에러(EOFError) 발생 -> 이유를 모르겠음
# rows, cols = map(int, input().split())

# matrix_a = []
# matrix_b = []

# for col in range(cols):
#     temp = list(map(int, input().split()))
#     matrix_a.append(temp)
    
# for col in range(cols):
#     temp = list(map(int, input().split()))
#     matrix_b.append(temp)

# for col in range(cols):
#     sum_matrix = ''
#     for row in range(rows):
#         sum_matrix += str((matrix_a[col][row] + matrix_b[col][row])) + ' '
#     print(sum_matrix)

## 새로운 풀이
N, M = map(int, input().split())

matrix_a = []
matrix_b = []

for i in range(N):
    temp = list(map(int, input().split()))
    matrix_a.append(temp)

for i in range(N):
    temp = list(map(int, input().split()))
    matrix_b.append(temp)
    
for i in range(N):
    new_matrix = ''
    for j in range(M):
        matrix_a[i][j] = matrix_a[i][j] + matrix_b[i][j]
        new_matrix += str(matrix_a[i][j]) + ' '
    print(new_matrix)

## 아래 방법으로도 같은 출력값 나온다
# for i in range(N):
#     for j in range(M):
#         matrix_a[i][j] = matrix_a[i][j] + matrix_b[i][j]

# for i in matrix_a:
#     print(*i)