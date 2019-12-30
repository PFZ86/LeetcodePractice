# https://www.youtube.com/watch?v=n_t0a_8H8VY
# Method 1: Use disjoint set; O(|V|) space; O(|V|) time.
def hasCycle(self, G):
    for v in G.vertex():
        makeSet(v)

    for (u, v) in G.edge():
        if findSet(u) == findSet(v):
            return True
        else:
            union(u, v)

    return False

# https://www.youtube.com/watch?v=6ZRhq2oFCuo
# Method 2: DFS. The trick is to pass the parent information in dfs.
# For every visited vertex v, if there is a neighbor u such that u
# is already visited and u is not a parent of v, then there is a cycle.
def hasCycle_helper(self, G, current, parent, visited):
    visited.append(current)

    for u in G.neighbor(current):
        # if u is not visited, then recur for u
        if u not in visited:
            if self.hasCycle_helper(G, u, current, visited):
                return True
        # if u is visited and not a parent of the current vertex,
        # then there is a cycle
        elif u != parent:
            return True

    return False

def hasCycle(self, G):
    visited = []

    for v in G.vertex():
        if v not in visited:
            if self.hasCycle_helper(G, v, None, visited):
                return True

    return False
