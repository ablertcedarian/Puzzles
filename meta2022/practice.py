""" 
You are planning a visit to an amusement park with three friends and need to decide which rollercoasters you want to go on. 
The park is a big crowded place, so they insist you visit the rollercoasters in the order laid out on the map.
Each of your friends has their own special way of picking which amusements they would like to visit, 
it's your job to help them figure out how much fun they are going to have at the amusement park, based on their respective strategies.
Your friend, Bob wants each rollercoaster he goes on to be strictly scarier than the previous he went on and he doesn't want to travel far between rollercoasters he goes on.
In particular, 
    Bob must visit rollercoasters in the same relative order that they appear on the map, 
    and if he chooses to go on a certain rollercoaster, then the next one he goes on (if any) must be the immediately following one. 

For example, he may choose to go on the 3rd and 4th rollercoasters, or on the 3rd, 4th, and 5th rollercoasters, but not on just the 3rd and 5th rollercoasters.
Like Alice, Bob has 10 units of fun for each rollercoaster he goes on, and he wants to maximize the amount of fun he has.

Your input is a file with K lines. 
The ith line contains a single integer representing the scariness of the ith rollercoaster. 
The rollercoasters are given in the order in which they appear on the amusement park map.

Output a single integer, the maximum amount of fun which Bob can have on the trip.
"""

name = "practice"

rollerCoasters = []

with open(name+"Input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        rollerCoasters.append(int(line.strip()))

scariest = 0
maxFun = 0
live = False 
currFun = 0 

for coaster in rollerCoasters:
    if not live:
        live = True 
        currFun += 10
        scariest = max(coaster, scariest) 
    else:
        if coaster > scariest:
            currFun += 10
            scariest = coaster 
        else:
            live = False 
            currFun = 10
            scariest = coaster 
        
        maxFun = max(maxFun, currFun)

with open(name+"Result.txt", "w") as f:
    f.write(str(maxFun))




