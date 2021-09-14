import json

def ucitaj_graf(fajl):
    try:
        with open(fajl, "r") as f:
            podaci = json.load(f)
            return dict(podaci)
    except:
        print("Greska")
        return None

#heuristika
def h(n):
    H = {
        "Oradea" : 380,
        "Zerind" : 374,
        "Arad" : 366,
        "Timisoara" : 329,
        "Lugoj" : 244,
        "Mehadia" : 241,
        "Drobeta" : 242,
        "Sibiu" : 253,
        "Fagaras" : 176,
        "Rimnicu Vilacea" : 193,
        "Pitesti" : 100,
        "Craiova" : 160,
        "Buchares" : 0
    }
    return H[n]

#algoritam
def astar(G, start, stop):
    open_list = set([start])
    closed_list = set([])

    g = {}
    parents = {}

    g[start] = 0
    parents[start] = None 

    while len(open_list) > 0:
        n = None 
        for v in open_list:
            if n == None or g[v]+h(v) < g[n]+h(n):
                n = v 

        if n == None:
            print("Trazeni put ne postoji")
            return None 
        
        if n == stop:
            path = []
            path.append(stop)
            tmp = parents[stop]
            while tmp != None:
                path.append(tmp)
                tmp = parents[tmp]
            path.reverse()
            return path

        for m, weight in G[n]:
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

        open_list.remove(n)
        closed_list.add(n)

    print("Trazeni put ne postoji")
    return None                     


def main():
    G = ucitaj_graf("cities.json")
    print(astar(G, "Arad", "Buchares"))

if __name__ == "__main__":
    main()
