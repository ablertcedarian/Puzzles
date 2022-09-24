from collections import defaultdict 
from decimal import Decimal 

name = "rexWages"
input = []
with open(name+"Input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        input.append(line.strip())

testCaseCount = int(input[0])
input = input[1:]

with open(name+"Result.txt", "w") as f:
    for testCountNum in range(testCaseCount):
        print(f"genius {testCountNum}, {testCaseCount}")
        firstLine = input[0].split(" ")
        N = int(firstLine[0])
        Q = int(firstLine[1])

        employees = list(map(int, input[1].split(" ")))
        # print(N, Q, employees)
        for line in input[2:2+Q]:
            vals = list(map(int, line.split(" ")))
            # print(vals)
            if vals[0] == 1:
                r = vals[-1]
                e = vals[-2]
                p1, p2, p3 = vals[1], vals[2], vals[3]
                # print(e, r, p1, p2, p3)
                for _ in range(r):
                    for enum in range(len(employees)):
                        currWage = employees[enum] 
                        if 0 <= currWage and currWage < 10**6:
                            # if enum == e-1:
                            #     print(str(currWage*(p1/100)))
                            newWage = currWage + currWage * (p1/100)
                        elif 10**6 <= currWage and currWage < 2*10**6:
                            # if enum == e-1:
                            #     print(str(currWage*(p2/100)))
                            newWage = currWage + currWage * (p2/100)
                        else:
                            # if enum == e-1:
                            #     print(f"funky {currWage}, {str(currWage*(p3/100))}")
                            newWage = currWage + currWage * (p3/100)
                        employees[enum] = newWage 
                        if enum == e-1:
                            # print(f"{enum}: {currWage} -> {newWage}, {p1}")
                            f.write('{:.6f}\n'.format(round(newWage, 6)))
            elif vals[0] == 2:
                e1, e2 = vals[1], vals[2]
                f.write('{:.6f}\n'.format(round(sum(employees[e1-1:e2]), 6)))
        
        input = input[2+Q:]
        # print()

