import math

class Maze:
    def __init__(self, maze_matrix):
        self.start, self.finish, self.adjacency_list = self.convert_to_graph(maze_matrix)
        self.maze_matrix = maze_matrix

    def __str__(self):
        return str(self.adjacency_list)    

    def convert_to_graph(self, maze_matrix):
        adjacency_list = {}
        start = None 
        finish = None 

        n = len(maze_matrix)
        m = len(maze_matrix[0])

        for i in range(n):
            for j in range(m):
                v = (i, j)
                neighbors = []
                if maze_matrix[i][j] != "X":
                    if maze_matrix[i][j] == "S":
                        start = v 
                    if maze_matrix[i][j] == "F":
                        finish = v
                    #gore
                    if i > 0:
                        if maze_matrix[i-1][j] != "X":
                            w = (i-1, j)
                            if maze_matrix[i-1][j] == "#":
                                weight = 2
                            else:
                                weight = 1
                            neighbors.append((w, weight))
                    #dole
                    if i < n-1:
                        if maze_matrix[i+1][j] != "X":
                            w = (i+1, j)
                            if maze_matrix[i+1][j] == "#":
                                weight = 2
                            else:
                                weight = 1
                            neighbors.append((w, weight))
                    #levo
                    if j > 0:
                        if maze_matrix[i][j-1] != "X":
                            w = (i, j-1)
                            if maze_matrix[i][j-1] == "#":
                                weight = 2
                            else:
                                weight = 1
                            neighbors.append((w, weight))
                    #desno
                    if j < m-1:
                        if maze_matrix[i][j+1] != "X":
                            w = (i, j+1)
                            if maze_matrix[i][j+1] == "#":
                                weight = 2
                            else:
                                weight = 1
                            neighbors.append((w, weight))

                adjacency_list[v] = neighbors
        return start, finish, adjacency_list                        


    #heuristika
    def h(self, cords):
        x = int(cords[0])
        y = int(cords[1])

        finish_x = int(self.finish[0])
        finish_y = int(self.finish[1])

        #return abs(x - finish_x) + abs(y - finish_y)              #menhetn

        #return math.sqrt( (x - finish_x)**2 + (y - finish_y)**2 ) #euklidsko

        return max(abs(x - finish_x), abs(y - finish_y))           #cebisevljevo
    

    #algoritam
    def astar(self, start, stop):
        open_list = set([start])
        closed_list = set([])

        g = {}
        parents = {}

        g[start] = 0
        parents[start] = None 

        brojac_iteracija = 0
        while len(open_list) > 0:
            n = None 
            for v in open_list:
                if n == None or g[v]+self.h(v) < g[n]+self.h(n):
                    n = v 
            
            if n == None:
                return None

            if n == stop:
                path = []
                path.append(stop)
                tmp = parents[stop]
                while tmp != None:
                    path.append(tmp)
                    tmp = parents[tmp]
                path.reverse()
                return (path, brojac_iteracija) 

            for m, weight in self.adjacency_list[n]:
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

            brojac_iteracija += 1              

        return None    
    
 
    def solve(self):
        graph_path, brojac_iteracija = self.astar(self.start, self.finish)
        if graph_path == None:
            print("Trazeni put ne postoji")
        else:
            print(brojac_iteracija)
            return graph_path


def main():
    maze_matrix = [["S", "#", "."],
                   [".", "X", "."],
                   [".", "#", "F"]]
    maze = Maze(maze_matrix)
    print(maze.solve())
    
if __name__ == "__main__":
    main()
