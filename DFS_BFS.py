from Stack import Stack
from Queue import Queue

class BFS_DFS:
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def __init__(self):
        with open("maze2.txt") as file:
            contents = file.readlines()
            self.height = len(contents)
            self.width = len(contents[0]) - 1
            self.parent = {}

        self.maze = []
        for i, line in enumerate(contents):
            tmp = []
            for j, ch in enumerate(line):
                if ch == "#":
                    tmp.append(-1)
                elif ch == " ":
                    tmp.append(0)
                elif ch == "A":
                    tmp.append("A")
                    self.start = (i, j)
                elif ch == "B":
                    tmp.append("B")
                    self.end = (i, j)
                elif ch == "\n":
                    continue
                else:
                    raise Exception("Unknown character encountered!")
            self.maze.append(tmp)
    
    def print(self, showExplored = False):
        for line in self.maze:
            for ch in line:
                if ch == -1:
                    print("█", end = "")
                elif ch == "A":
                    print("A", end = "")
                elif ch == "B":
                    print("B", end = "")
                elif ch == 0 or ch == 1:
                    print(" ", end = "")
                elif ch == 3:
                    print("*", end = "")
                elif showExplored == True and ch == 2:
                    print("*", end = "")
                elif showExplored == False and ch == 2:
                    print(" ", end = "")
                else:
                    raise Exception("Unknown character encountered!")
            print()
    
    def getNeighbours(self, state):
        i, j = state
        neighbours = []
        for move in BFS_DFS.moves:
            x, y = move
            # print(x, y)
            if ((i + x) >= 0 and (i + x) < self.height) and ((j + y) >=0 and (j + y) < self.width) and (self.maze[i + x][j + y] == 0 or self.maze[i + x][j + y] == "B"):
                neighbours.append((i + x, j + y))
                if self.maze[i + x][j + y] == 0:
                    self.maze[i + x][j + y] = 1
                self.parent[(i + x, j + y)] = (i, j)
            else:
                continue
        
        return neighbours
    
    def markPath(self):
        state = self.end

        while self.parent[state]:
            i, j = self.parent[state]
            if self.maze[i][j] != "A":
                self.maze[i][j] = 3
            state = self.parent[state]
    
    def solve(self):
        s = Queue()
        s.push(self.start)
        self.num_explored = 0
        self.parent[self.start] = None

        while s.front():
            pi, pj = s.front()
            self.num_explored += 1
            s.pop()
            if self.maze[pi][pj] != "A" and self.maze[pi][pj] != "B":
                self.maze[pi][pj] = 2
            if self.end == (pi, pj):
                self.markPath()
                break
            for neighbour in self.getNeighbours((pi, pj)):
                s.push((neighbour))




def main():
    obj = BFS_DFS()
    obj.print()
    print()
    print("SOLVING...")
    obj.solve()
    print("Number of state explored: ", obj.num_explored)
    obj.print(showExplored = True)


if __name__ == "__main__":
    main()