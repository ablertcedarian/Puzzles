import sys
from collections import defaultdict 

T = int(sys.stdin.readline())

def genDFS(badPairs, stack, path, current):
    # print(f"Gen dfs, {stack}, {path}, {current}")
    # Color pair is bad 
    if len(path) >= 1 and path[-1] in badPairs[current]:
        return 0
    path += [current] 
    
    # Check if done
    if len(stack) == 0:
        # print(f"Gen dfs solution {path}") 
        return 1
    
    resCount = 0 
    for i in range(len(stack)):
        color = stack.pop(i) 
        count = genDFS(badPairs, stack.copy(), path.copy(), color)
        resCount += count 
        # print(f"in gen dfs {stack}")
        stack = stack[:i] + [color] + stack[i:]
        # print(f"in gen dfs2 {stack}")
    
    return resCount 
    
def specDFS(badPairs, stack, path, current):
    # print(f"Spec dfs, {stack}, {path}, {current}")
    # Color pair is bad 
    if len(path) >= 1 and path[-1] in badPairs[current]:
        return None 
    path += [current] 
    
    # Check if done
    if len(stack) == 0:
        return ' '.join(path)
    
    done = False
    i = 0 
    while not done and i < len(stack):
        color = stack.pop(i) 
        res = specDFS(badPairs, stack.copy(), path.copy(), color)
        if res is not None:
            return res  
        stack = stack[:i] + [color] + stack[i:]
        i += 1 
    return None 

for testCase in range(T):
    N = int(sys.stdin.readline())
    colors = sys.stdin.readline().strip('\n').split(" ")
    M = int(sys.stdin.readline())
    badPairs = defaultdict(list)
    for badPair in range(M):
        pair = sys.stdin.readline().strip('\n').split(" ")
        badPairs[pair[0]] += [pair[1]]
        badPairs[pair[1]] += [pair[0]]
    # print(badPairs) 

    solutions = 0
    painting = "" 
    
    # Get count of valid paintings
    for i in range(len(colors)):
        head = colors.pop(i)
        solutions += genDFS(badPairs, colors.copy(), [], head)
        # print(colors) 
        colors = colors[:i] + [head] + colors[i:]
        # print(colors)
    
    print(solutions)

    # Get best painting 
    for i in range(len(colors)):
        head = colors.pop(i)
        solution = specDFS(badPairs, colors.copy(), [], head)
        if solution is not None:
            painting = solution
            break 
        colors = colors[:i] + [head] + colors[i:]    
    
    print(painting) 
    
    
    
        
    

        