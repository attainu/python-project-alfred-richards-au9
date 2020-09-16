# Maze Solver Project
def Display(visited):
    print('Solved maze path:')
    for i in visited:
        for j in i:
            print(str(j)+' ',end='')
        print('')
def Find_path(Graph,Row):
    visited=[[0 for i in range(Row)] for i in range(Row)]
    if Maze_Path(Graph,0,0,visited,Row):
        Display(visited)
    else:
        print('Path doesnt exist')

def Validate_path(Graph,x,y,visited,Row):
    if x>=0 and x<Row and y >=0 and y<Row and Graph[x][y]==1:
        return True
    else:
        return False

def Maze_Path(Graph,x,y,visited,Row):
    if x==Row-1 and y==Row-1:
        visited[x][y]=1
        return True
    if Validate_path(Graph,x,y,visited,Row):
        visited[x][y]=1
        if Maze_Path(Graph,x+1,y,visited,Row):
            return True
        if Maze_Path(Graph,x,y+1,visited,Row):
            return True

if __name__ == "__main__":
    Graph=[]
    Row=int(input('Enter number of rows\n'))
    for i in range(Row):
        print('Enter row:',i+1)
        row=list(map(int,input().split()))
        Graph.append(row)
    Find_path(Graph,Row)

