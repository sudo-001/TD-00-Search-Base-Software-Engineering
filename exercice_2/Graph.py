from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Add an edge between u and v."""
        if u not in self.graph:
            self.graph[u] = [] # Create an empty list for the vertex u
        if v not in self.graph:
            self.graph[v] = [] # Create an empty list for the vertex v
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        """Breadth First Search starting from the vertex start."""
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph[node])
        
        return result
    
    def dfs(self, start, visited=None):
        """Depth First Search DFS (recursive)"""
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
        
    def is_connected(self, start, end):
        """Verify if two nodes are connected (via BFS) and return the shortest path"""
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path # path found
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    queue.append((neighbor, path + [neighbor]))

        return None # No path found
        
    def load_from_file(self, filename):
        """Load a graph from a file."""
        try:
            with open(filename, "r") as file:
                for line in file:
                    if "->" in line:
                        u, v = map(str.strip, line.strip().split("->"))
                        self.add_edge(u, v)
        except FileNotFoundError:
            print(f"File {filename} not found.")