#jun2 2018/2019

from collections import deque

class Graph:
    # Funkcija vraca listu susednih stanja tekuceg stanja
    def get_neighbors(self, v):
        neighbors = []
        
        #=== Studentski kod ===#
        n = len(v)
        for i in range(n-1):
            for j in range (i, n+1):
                left = v[:i]
                middle = v[i:j]
                right = v[j:]
                neighbor = left + middle[::-1] + right
                neighbors.append((neighbor, 1))
        return neighbors 
    
    # Funkcija pronalazi put od stanja start do stanja stop
    # koriscenjem BFS pretrage
    def bfs(self, start, stop):
        #=== Studentski kod ===#
        red = deque([start])
        
        parent = {}
        # Kastovanjem u str se vrsi serijalizacija
        parent[str(start)] = None
        
        while len(red) > 0:
        #=== Studentski kod ===#
            n = red.popleft()    
            
            if n == stop:
                path = [stop]
                tmp = parent[str(n)]
                while tmp != None:
                    path.append(tmp)
                    tmp = parent[str(tmp)]
                path.reverse()
                return path

            for m, _ in self.get_neighbors(n):
                if str(m) not in parent:
                    #=== Studentski kod ===#
                    parent[str(m)] = n 
                    red.append(m)
                    
        print('Trazeni put nije pronadjen')
        return None


def main():
    g = Graph()

    start = ['H', 'D', 'F', 'G', 'A', 'E', 'B', 'C']
    stop  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    path = g.bfs(start, stop)

    for state in path:
        print(state)
    print()
    print('Tajna poruka je: {}'.format(len(path) - 1))


if __name__ == "__main__":
    main()
