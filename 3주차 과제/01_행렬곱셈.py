# 4행 3열 행렬
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# 3행 2열 행렬
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# 행렬의 크기
rows_a = len(A)
cols_a = len(A[0])

rows_b = len(B)
cols_b = len(B[0])

# 행렬 곱셈 가능 여부 확인
if cols_a != rows_b:
    raise ValueError("A의 열 개수와 B의 행 개수가 같아야 합니다.")

# 결과 행렬 C 생성
C = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

# 행렬 곱셈
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            C[i][j] += A[i][k] * B[k][j]

# 결과 출력
print("A × B =")
for row in C:
    print(row)