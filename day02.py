# Lose = 0 - (X)
# Draw = 3 - (Y)
# Win = 6 - (Z)
# Rock = 1 - A, X
# Paper = 2 - B, Y
# Scissors = 3 - C, Z

points = 0
points2 = 0

def winner(opp, me):
    if(opp == "A" and me == "X" or
         opp == "B" and me == "Y" or
         opp == "C" and me == "Z"):
        return 3
    elif(opp == "A" and me == "Y" or
         opp == "B" and me == "Z" or
         opp == "C" and me == "X"):
         return 6
    else:
        return 0

def hand(opp, res):
    if(opp == "A" and res == "Y" or
       opp == "B" and res == "X" or
       opp == "C" and res == "Z"):
       return 1
    elif(opp == "A" and res == "Z" or
       opp == "B" and res == "Y" or
       opp == "C" and res == "X"):
       return 2
    elif(opp == "A" and res == "X" or
       opp == "B" and res == "Z" or
       opp == "C" and res == "Y"):
       return 3

with open("inputs/day02_input.txt") as file:
    lines = [line.rstrip() for line in file]
for line in lines:
    opp,me = line.strip().split()
    if(me == "X"):
        points = points + winner(opp, me) + 1
    elif(me == "Y"):
        points = points + winner(opp, me) + 2
    elif(me == "Z"):
        points = points + winner(opp, me) + 3
# print(points)
    if(me == "X"):
        points2 = points2 + hand(opp, me) + 0
    elif(me == "Y"):
        points2 = points2 + hand(opp, me) + 3
    elif(me == "Z"):
        points2 = points2 + hand(opp, me) + 6
print("ponits2: ",points2)
