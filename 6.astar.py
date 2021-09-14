#jun1 2018/2019

class Graph:
    def __init__(self, elements, target):
        self.elements = elements # Raspolozivi brojevi
        self.target = target     # Ciljni zbir
    
    # Funkcija vraca niz susednih stanja u obliku (w, e)
    # gde je w susedno stanje a e duzina grane od cvora v
    # do cvora w
    def get_neighbors(self, v):
        neighbors = []
    
        #=== Studentski kod ===#
        for element in self.elements:
            neighbor = (v + element, element)
            neighbors.append(neighbor)
        
        return neighbors
    
    
    def h(self, v):
        #=== Studentski kod ===#
        return abs(self.target - v)
    
    
    def astar(self, start):
        
        #=== Studentski kod ===#
        open_list = set([start])
        closed_list = set([])
        
        g = {}
        parents = {}

        g[start] = 0
        parents[start] = None 

        while len(open_list) > 0:
            n = None 
            for v in open_list:
                if n == None or g[v]+self.h(v) < g[n]+self.h(n):
                    n = v 

            if n == None:
                return None 

            if n == self.target:
                #=== Studentski kod ===#
                path = []
                path.append(n)
                tmp = parents[n]
                while tmp != None:
                    path.append(tmp)
                    tmp = parents[tmp]
                path.reverse()
                return path 

            for m, weight in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n 
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
    elements = [1, 2, 3, 5, 8]
    g = Graph(elements, 15)
    path = g.astar(0)
    
    if path != None:
        n = len(path)
        for i in range(1, n):
            print('{}. sabirak: {}'.format(i, path[i] - path[i - 1]))
    else:
        print("Trazeni put ne postoji")


if __name__ == "__main__":
    main()
