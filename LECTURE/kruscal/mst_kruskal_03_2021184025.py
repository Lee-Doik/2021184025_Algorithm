n_vertices = 12

edges = [
(0, 6, 194), (0, 7, 59), (0, 9, 372), (1, 11, 125), (2, 4, 345), 
(2, 8, 246), (2, 9, 293), (2, 10, 166), (4, 8, 82), (4, 10, 164), 
(5, 6, 119), (5, 7, 232), (6, 7, 169), (8, 9, 286), (8, 10, 193), 
(9, 10, 150) ]


sorted_edges = sorted(edges, key = lambda e:e[2])
current_edge_index = 0
mst = []
roots = [r for r in range(n_vertices)]

def find_root(v):
	root = roots[v]
	if v !=  roots[v]:
		roots[v] = find_root(root)		# 경로압축
	return roots[v]

def union(u,v):
	ur = find_root(u)
	vr = find_root(v)
	roots[vr] = ur

n_edges = len(edges)
for current_edge_index in range(n_edges):
	u, v, w = sorted_edges[current_edge_index]
	mst.append((u, v, w))
	if u == v:
		continue
		
	if len(mst) >= n_vertices - 1: break


print(f"mst = {mst}")