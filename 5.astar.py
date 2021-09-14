#septembar 2019/2020

mapa = [[5, 20, 100, 30, 20, 14, 1, 2, 7, 1],
        [1, 33, 14, 15, 16, 200, 33, 99, 5, 2],
        [3, 4, 8, 9, 30, 300, 33, 44, 11, 555],
        [8, 10, 12, 14, 33, 9, 8, 1, 1, 1],
        [60, 3, 1, 1, 1, 1, 1, 1, 1, 1],
        [30, 40, 50, 70, 10, 1, 2, 3, 7, 6],
        [4, 5, 1, 80, 90, 1, 1, 10, 11, 12],
        [33, 44, 10, 10, 1, 3, 8, 6, 7, 1],
        [5, 5, 6, 1, 1, 4, 8, 10, 11, 5],
        [1, 80, 3, 3, 3, 3, 12, 200, 33, 4]]


class Graph:
    def __init__(self, mapa):
        self.mapa = mapa
        
    def valid(self, i, j):
        if i >= 0 and j >= 0 and i < 10 and j < 10:
            return True
        else:
            return False        
        
    # i i j su koordinate trenutnog polozaja figure na mapi
    # Funkcija vraca sve gde figura moze da skoci
    def get_neighbors(self, i, j):
        susedi = []
        
        indeksi = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for indeks in indeksi:
            if self.valid(i+indeks[0], j+indeks[1]):
                susedi.append((i+indeks[0], j+indeks[1]))
            
        return susedi
    

    # Heuristika
    def h(self, i, j):
        #=== Studentski kod ===#
        return ((9-i) + (9-j)) / 3
    

    # Pronalazenje najkraceg puta pomocu algoritma A*
    def astar(self):

        # Zatvorena lista je inicijalno prazna, a otvorena lista sadrzi samo polazni cvor 
        # Kako figura krece sa pozicije 0,0 polazni cvor je (0, 0)
        open_list = set([(0, 0)])
        closed_list = set([])

        # g sadrzi tekuce udaljenosti od polaznog cvora (start) do ostalih cvorova, ukoliko se cvor ne nalazi
        # u mapi, podrazumevana vrednost udaljenosti je beskonacno
        g = {}
        
        # Mapa parents cuva roditelje cvorova
        parents = {}

        #=== Studentski kod ===#
        g[(0, 0)] = 0
        parents[(0, 0)] = None 

        while len(open_list) > 0:
            n = None 
            for v in open_list:
                if n == None or g[v] + self.h(v[0], v[1]) < g[n] + self.h(n[0], n[1]):
                    n = v 
            
            if n == None:
                return None

            if n == (9, 9):
                suma = 0
                suma += mapa[9][9]
                path = []
                path.append(n)
                tmp = parents[n]
                while tmp != None:
                    suma += mapa[tmp[0]][tmp[1]]
                    path.append(tmp)
                    tmp = parents[tmp]
                path.reverse()
                return (path, suma)

            for m in self.get_neighbors(n[0], n[1]):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n 
                    g[m] = g[n] + mapa[m[0]][m[1]]
                else:
                    if g[n] + mapa[m[0]][m[1]] < g[m]:
                        g[m] = g[n] + mapa[m[0]][m[1]]
                        parents[m] = n 
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        return None 


def main():
    G = Graph(mapa)
    (putanja, cena) = G.astar()
    if putanja != None:
        print("Pronadjen je put {}".format(putanja))
        print("Minimalna cena je {}".format(cena))
    else:
        print("Trazeni put ne postoji")


if __name__ == "__main__":
    main()    
