#         [C] [B] [H]                
# [W]     [D] [J] [Q] [B]            
# [P] [F] [Z] [F] [B] [L]            
# [G] [Z] [N] [P] [J] [S] [V]        
# [Z] [C] [H] [Z] [G] [T] [Z]     [C]
# [V] [B] [M] [M] [C] [Q] [C] [G] [H]
# [S] [V] [L] [D] [F] [F] [G] [L] [F]
# [B] [J] [V] [L] [V] [G] [L] [N] [J]
#  1   2   3   4   5   6   7   8   9 

#proc-[1]----[3]--[5]
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

creates = [['W','P','G','Z','V','S','B'],
           ['F','Z','C','B','V','J'],
           ['C','D','Z','N','H','M','L','V'],
           ['B','J','F','P','Z','M','D','L'],
           ['H','Q','B','J','G','C','F','V'],
           ['B','L','S','T','Q','F','G'],
           ['V','Z','C','G','L'],
           ['G','L','N'],
           ['C','H','F','J']]

with open("inputs/day05_input.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    proc = line.split()
    for i in range(int(proc[1]),0,-1):
        if(i == 0):
            break
        x = creates[(int(proc[3])-1)].pop(0)
        #creates[(int(proc[5])-1)].insert(0, x)
        j = int(proc[1])-i
        creates[(int(proc[5])-1)].insert(j, x)
for create in creates:
    print(create[0],end="")
