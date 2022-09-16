from collections import defaultdict 

name = "day1"

input = []

with open(name+"Input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        input.append(line.strip())

numGraphs = int(input[0])

graphs = [[] for _ in range(numGraphs)]

graphNum = 0
for line in input[1:]:
    if line == "":
        graphNum += 1
    else:
        graphs[graphNum].append(line.split(" "))

allNums = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1}

def deduceZig(graph, zigNum = 0):
    allNumsZig = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1}

    # traverse the Zig
    point = [0, zigNum]

    holes = []
    for i in range(9):
        point[0] = (point[0] + 1) % 9
        point[1] = (point[1] + 1) % 9
        # print(point[0], point[1], len(graph), len(graph[0]))
        val = graph[point[0]][point[1]]
        if val.isdigit():
            del allNumsZig[int(val)]
        else:
            holes.append(point)

    return list(allNumsZig.keys()), holes 

def deduceZag(graph, zagNum = 0):
    allNumsZag = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1}

    point = [0, zagNum]

    holes = []
    for i in range(9):
        point[0] = (point[0] + 1) % 9
        point[1] = (point[1] - 1) % 9
        # print(point)
        val = graph[point[0]][point[1]]
        if val.isdigit():
            del allNumsZag[int(val)]
        else:
            holes.append(point)

    return list(allNumsZag.keys()), holes

def deduceSquare(graph, squareNum = 0):
    allNumsSquare = {0:1,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1}

    pointBase = [(squareNum // 3)*3, (squareNum % 3)*3]
    point = [0,0]

    holes = []
    for i in range(9):
        point[0] = pointBase[0] + (i // 3)
        point[1] = pointBase[1] + (i % 3)
        # print(point)
        val = graph[point[0]][point[1]]
        if val.isdigit():
            del allNumsSquare[int(val)]
        else:
            holes.append(point)
    
    return list(allNumsSquare.keys()), holes

def checkGraph(graph):
    zigPoss, zigHoles = deduceZig(graph)
    zagPoss, zagHoles = deduceZag(graph)
    squarePoss, squareHoles = deduceSquare(graph)

    poss = []
    zigAndSquare = []
    for x in range(8, -1, -1):
        if x in zigPoss and x in zagPoss and x in squarePoss:
            poss.append(x)
        elif x in zigPoss and x not in zagPoss and x in squarePoss:
            zigAndSquare.append(x) 

    if len(poss) == 1:
        return poss[0]

totalSum = 0
for graph in graphs:
    graphRes = checkGraph(graph)
    totalSum += graphRes
    print(f"Solved! {graphRes}")

print(totalSum)

res = totalSum

with open(name+"Result.txt", "w") as f:
    f.write(str(res))