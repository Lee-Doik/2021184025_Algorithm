from collections import defaultdict
from heapdict import heapdict
n_vertices = 12

edges = [
(0, 6, 194), (0, 7, 59), (0, 9, 372), (1, 11, 125), (2, 4, 345), 
(2, 8, 246), (2, 9, 293), (2, 10, 166), (4, 8, 82), (4, 10, 164), 
(5, 6, 119), (5, 7, 232), (6, 7, 169), (8, 9, 286), (8, 10, 193), 
(9, 10, 150), (3, 4, 100), (3, 8, 200), (1, 5, 150), (5, 11, 250) ]

g = defaultdict(dict)
for u, v, w in edges:
	#edges의 내용을 g 로 옮김(adj-matrix의 형태로)
	g[u][v] = w
	g[v][u] = w

# def print_adj_matrix():
#   for u in range(n_vertices):
#     for v in range(n_vertices):
#       w = g[u][v] if v in g[u] else 0
#       print(f'{w:5d}', end='')
#     print()
#   print()
# print_adj_matrix()

D = heapdict()			# 거리만 저장함. key = 정점인덱스, value = 가중치
origins = dict()		# 어디로부터 왔는지 알 수있는 정보 key = 정점, value = 어디서 왔는지
tree_vertices = set()	# 완성된 결과에 포함된 정점들.

mst = [] # 결과물

start_index = 3
# INF = float('inf')
# for i in range(n_vertices):
# 	if i in g[start_index]:
# 		D[i] = g[start_index][i]
# 	else:
# 		D[i] = INF
# print(D)
tree_vertices.add(start_index)
D[start_index] = 0
origins[start_index] = start_index
total_weight = 0
while D:
	k, v = D.popitem()
	orig = origins[k] # 점 K가 어디서 왔는지 알아낸다.
	if orig != k:
		mst.append((orig, k, v))
		tree_vertices.add(k)
		total_weight += w

	for adj, weight in g[k].items():
	# K에서 연결되는 점들에 대해 adj 점까지 weight 비용으로 연결된다.
		if adj in tree_vertices: continue	# 이미 결과  tree 에 있는 점이면 거르고 실행
		if adj in D and D[adj] < weight: continue # 이미 비용이 덜 드는 점이면 거른다.
		D[adj] = weight # 비용을 업데이트 한다.
		origins[adj] = k #adj 까지는 k를 통해서 오는 것이 가장 싸다.

print(origins)
for i in range(n_vertices):
	path = str(i)
	orig = i
	while origins[orig] != orig:
		path = f'{origins[orig]} - {path}'
		orig = origins[orig]
	print (path)

print(f"mst = {mst} \nTotal Weight = {total_weight} ")
