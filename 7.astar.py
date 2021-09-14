#jun1 2018/2019

class Graph:
        
    # Funkcija pretvara listu v u tekstualni oblik
    # [1,2,3] -> "1,2,3"
    def serialize(self, v):
        return ','.join([str(x) for x in v])
    
    # Funkcija pretvara v iz tekstualnog oblika u listu
    # "1,2,3" -> [1,2,3]
    def deserialize(self, v):
        return [int(x) for x in v.split(',')]
        
    # Funkcija vraca niz susednih stanja u obliku (w, e)
    # gde je w susedno stanje a e duzina grane od cvora v
    # do cvora w
    def get_neighbors(self, v):
        w = self.deserialize(v)
        neighbors = []
        
        #=== Studentski kod ===#
        n = len(w)
        for i in range(n):
            neighbor = w[:]
            neighbor[i] = (neighbor[i] - 1 + 5) % 14 + 1
            neighbors.append((self.serialize(neighbor), 1))
        return neighbors

    
    # Funkcija heuristicke procene udaljenosti od stanja v
    # do ciljnog stanja
    def h(self, v):
        w = self.deserialize(v)
        #=== Studentski kod ===#
        return len(set(w))
    

    # Funkcija pronalazi put od start stanja do ciljnog stanja
    # koriscenjem a* algoritma
    def astar(self, start):
        open_list = set([self.serialize(start)])
        closed_list = set([])

        #=== Studentski kod ===#
        g = {}
        parent = {}

        g[self.serialize(start)] = 0
        parent[self.serialize(start)] = None 
                
        #=== Studentski kod ===#
        while len(open_list) > 0:
            n = None 
            for v in open_list:
                if n == None or g[v]+self.h(v) < g[n]+self.h(n):
                    n = v 
                
            if n == None:
                return None 

            #=== Studentski kod ===#
            if len(set(self.deserialize(n))) == 1:
                path = []
                path.append(n)
                tmp = parent[n]
                while tmp != None:
                    path.append(tmp)
                    tmp = parent[tmp]
                path.reverse()
                return path 
            
            #=== Studentski kod ===#
            for m, weight in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parent[m] = n 
                    g[m] = g[n] + weight
                else:
                    if g[n] + weight < g[m]:
                        g[m] = g[n] + weight
                        parents[m] = n 
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m) 
            
            #=== Studentski kod ===#
            open_list.remove(n)
            closed_list.add(n)
        
        return None


def main():
    g = Graph()
    path = g.astar([5, 10, 1])
    if path != None:
        for element in path:
            print(element)
    else:
        print("Trazeni put ne postoji")
    

if __name__ == "__main__":
    main()
