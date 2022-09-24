from collections import defaultdict 

name = "thermalLake"

input = []

with open(name+"Input", 'r') as f:
    lines = f.readlines()
    for line in lines:
        input.append(line.strip())

firstLine = input[0].split(" ")
N = int(firstLine[0])
Q = int(firstLine[1])

def area(a, b, c):
    return abs((a[0] * (b[1]-c[1]) + b[0] * (c[1]-a[1]) + c[0] * (a[1]-b[1])) / 2)

def sign(a, b, c):
    return (a[0]-c[0]) * (b[1]-c[1]) - (b[0]-c[0]) * (a[1]-c[1])

def halfPlane(dataCenter, triangle):
    d1 = sign(dataCenter, triangle[0], triangle[1])
    d2 = sign(dataCenter, triangle[1], triangle[2])
    d3 = sign(dataCenter, triangle[2], triangle[0])

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = ((d1 > 0) or (d2 > 0) or (d3 > 0))

    return not (has_neg and has_pos) 

def threeSlopes(dataCenter, triangle):
    a = triangle[2]
    b = triangle[0]
    x = dataCenter 

    if x == a or x == b or x == triangle[1]:
        return True 
    
    ydiff1 = a[1] - x[1]
    if ydiff1 > 0:
        slopebase = (a[1]-b[1])/(a[0]-b[0])
        slope1 = (a[1]-x[1])/(a[0]-x[0])
        if slope1 < slopebase:
            slope2 = (x[1]-b[1])/(x[0]-b[0])
            if slope2 > slopebase:
                return True 
        elif slope1 == slopebase:
            return True 
    return False 

def checkOutage(dataCenter, triangle):
    baseArea = baseAreas[str(triangle)]
    a1 = area(triangle[0], triangle[1], dataCenter)
    a2 = area(triangle[0], dataCenter, triangle[2])
    a3 = area(dataCenter, triangle[1], triangle[2])

    if baseArea == (a1+a2+a3):
        return True
    else:
        return False 

dataCenters = []
for line in input[1:1+N]:
    points = line.split(" ")
    dataCenters.append([int(points[0]), int(points[1])])

baseAreas = {}
triangles = []
horiLog = defaultdict(list)
vertLog = defaultdict(list) 
for i, line in enumerate(input[1+N:]):
    points = line.split(" ")
    # print(points)
    tria = [[int(points[0])+int(points[2]), int(points[1])],
            [int(points[0]), int(points[1])], 
            [int(points[0]), int(points[1])+int(points[2])]]
    baseAreas[str(tria)] = area(tria[0], tria[1], tria[2])
    for x in range(tria[1][0], tria[0][0]+1):
        horiLog[x] += [i]
    for y in range(tria[1][1], tria[2][1]+1):
        vertLog[y] += [i]
    triangles.append(tria) 

import time 
numCenters = len(dataCenters)
numTriangles = len(triangles)
with open(name+"Result2.txt", "w") as f:


    # triangleCount = 0
    # for triangle in triangles:
    #     rawCount = 0 
    #     count = 0
    #     start = time.time() 
    #     for dataCenter in dataCenters:
    #         if (dataCenter[0] >= triangle[1][0] and dataCenter[0] <= triangle[0][0] and 
    #             dataCenter[1] >= triangle[1][1] and dataCenter[1] <= triangle[2][1]):
    #             # if checkOutage(dataCenter, triangle):
    #             #     count += 1
    #             # if halfPlane(dataCenter, triangle):
    #             #     count += 1
    #             if threeSlopes(dataCenter, triangle):
    #                 count += 1

    #         rawCount += 1
    #     f.write(str(count) + '\n')
    #     end = time.time() 
    #     triangleCount += 1
    #     if triangleCount % 100 == 0:
    #         print(f"Triangle {triangleCount}/{numTriangles}, {int(triangleCount/numTriangles * 100)}%, took {end-start}")

