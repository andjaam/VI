#septembar 2018/2019

from queue import LifoQueue

class Graph:
    def __init__(self, fragments):
        # Svi DNK fragmenti
        self.fragments = fragments
        
        # Ukupan broj fragmenata
        self.num_fragments = len(fragments)
        
    def __str__(self):
        return str(self.adjacency_list)
    
    # Funkcija pronalazi sve susedne fragmente
    # tekuceg fragmenta
    def get_neighbors(self, fragment):
        neighbors = []
        
        #=== Studentski kod ===#
        for neighbor in self.fragments:
            if neighbor[0] == fragment[-1]:
                neighbors.append((neighbor, 1))
        return neighbors
    
    
    # Funkcija pokusava da sa svakim fragmentom
    # pocne sekvencu a redosled ostalih sekvenci,
    # ako takav postoji, pronalazi koriscenjem 
    # DFS pretrage
    def solve(self):
        for fragment in self.fragments:
            path = self.dfs(fragment)
            if path != None:
                return path
            
    # Funkcija vrsi DFS pretragu pocevsi od odabranog
    # start fragmenta i trazi put koji obuhvata sve
    # fragmente iz zadatog niza fragmenata
    def dfs(self, start):
        visited = {start}
        path = [start]
        
        while len(path) > 0:
        #=== Studentski kod ===#
            n = path[-1]

            if len(visited) == self.num_fragments:
                return path
            
            #=== Studentski kod ===#
            has_unvisited = False 

            for m, weight in self.get_neighbors(n):
                if m not in visited:
                    visited.add(m)
                    path.append(m)
                    has_unvisited = True
                    break
            
            if not has_unvisited:
                path.pop()
        
        return None


def main():
    fragments = ['CATG','TCGA', 'ACGG', 'GCGG', 'GATC']
    g = Graph(fragments)
    path = g.solve()

    n = g.num_fragments
    sequence = path[0]
    for i in range(1,n):
        sequence += path[i][1:]
    
    print('Redosled fragmenata: {}'.format(path))
    print('Kompletna sekvenca: {}'.format(sequence))


if __name__ == "__main__":
    main()    
