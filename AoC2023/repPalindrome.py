import sys


toPrint = "NO"
for i,line in enumerate(sys.stdin):
    if i == 0:
        if line.rstrip() == line.rstrip()[::-1]:
            toPrint = "YES"
    elif i == 1:
        print(toPrint)
    else:
        break
    