from scipy.spatial import KDTree
# KDTrees are a datastructure optimized for nearest neighbor queries.

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]


# KDTrees() are a datastructure optimized for nearest neighbor queries.
kdtree = KDTree(points)


# The query() method returns the distance to the nearest neighbor and the location of the neighbors.
res = kdtree.query((1, 1))

print(res)