#change the variable according to the task
task = 14

chars = []

with open("inputs/day06_input.txt") as file:
    lines = [line.rstrip() for line in file]

for i in range(len(lines[0])):
    chars.append(lines[0][i])
    for j in range(1,task):
        if(lines[0][i+j] in chars):
            chars.clear()
            break
        else:
            chars.append(lines[0][i+j])
    if(len(chars) == task):
        print(i+task)
        break
    

