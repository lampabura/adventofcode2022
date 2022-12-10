import re

with open("inputs/day07_input.txt") as file:
    lines = [line.rstrip() for line in file]


sizes = []
stack = []
res1 = 0
tmp = []
res2 = 0

for line in lines:
    if(line == "$ cd .."):
        folder = stack.pop()
        sizes.append(folder)
        stack[-1] += folder
    elif(line.startswith("$ cd")):
        stack.append(0)
    elif(line[0].isdigit()):
        val,n = line.split()
        stack[-1] += int(val)

while stack:
    folder = stack.pop()
    sizes.append(folder)
    if stack:
        stack[-1] += folder


needed = 30000000 - (70000000 - sizes[-1])
for i in sizes:
    if(i <= 100000):
        res1 += i
    if(i >= needed):
        tmp.append(i)
res2 = min(tmp)
    
print(res1)
print(res2)



