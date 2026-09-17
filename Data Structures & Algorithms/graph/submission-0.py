from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        if dst not in self.graph:
            self.graph[dst] = []
        if src not in self.graph:
            self.graph[src] = [dst]
        else:
            if dst not in self.graph[src]:
                self.graph[src].append(dst)
            else:
                return

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        else:
            if dst not in self.graph[src]:
                return False
            else:
                self.graph[src].remove(dst)
                return True

    def dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        if src not in self.graph:
            return False
        visited.add(src)
        for n in self.graph[src]:
            if n not in visited:
                if self.dfs(n, dst, visited):
                    return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)