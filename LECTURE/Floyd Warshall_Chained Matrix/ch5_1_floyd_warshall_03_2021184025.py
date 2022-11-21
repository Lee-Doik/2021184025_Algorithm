import sys

INF = sys.maxsize

n_vertices = 12
edges = [
    (0, 6, 194), (0, 7, 59), (0, 9, 372), (1, 11, 125), (2, 4, 345), 
    (2, 8, 246), (2, 9, 293), (2, 10, 166), (4, 8, 82), (4, 10, 164), 
    (5, 6, 119), (5, 7, 232), (6, 7, 169), (8, 9, 286), (8, 10, 193), 
    (9, 10, 150), (3, 4, 100), (3, 8, 200), (1, 5, 150), (5, 11, 250),
]

#함수는 사용하지 않고 작성한다.
#결과는 12x12의 표 형태로 출력한다.

# Edge list -> Adj matrix 형태로 변환
# 2차원 배열 D 에 0, 비용, inf 중 하나를 넣어 초기화
# K를 0부터 11가지 변환하며 비용 갱신
# 갱신할때 i 부터 j 까지 가려면 k로 가야한다 라는 내용도 추가(가산점)
# D의 내용을 출력한다.
# 12x12에 가까운 경로들을 모두 출력해도 좋다.(가산점)

g = [[INF]*n_vertices for i in range(n_vertices)]

for u, v, w in edges:
    g[u][v] = w
    g[v][u] = w

D = [[INF]*n_vertices  for i in range(n_vertices)]

for i in range(n_vertices):
    for j in range(n_vertices):
        D[i][j] = g[i][j]

for i in range(n_vertices):
    for j in range(n_vertices):
        if i == j:
            D[i][j] = 0


for k in range(n_vertices):
    for i in range(n_vertices):
        if k == i: continue
        for j in range(n_vertices):
            if i == j or k == j: continue
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][i]


for u in range(n_vertices):
    for v in range(n_vertices):
      w = D[u][v]
      print(f'{w:5d}', end='')
    print()
print()