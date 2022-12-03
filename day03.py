# a - z: 1-26  --  ascii- 96
# A - Z: 27-52  --  ASCII- 38
# RCMRQjLLWGTj nlnZwwnZJRZH
someone = 0
sum_two = 0

with open("inputs/day03_input.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    string1 = line[:len(line)//2]
    string2 = line[len(line)//2:]
    for i in string1:
        for j in string2:
            if(i == j and i.isupper()):
                someone = someone + ord(i) - 38
                break
            elif(i == j and i.islower()):
                someone = someone + ord(i) - 96
                break
        if(i == j):
            break
#print(sum)

for n in range(0,len(lines),3):
    string1 = lines[n]
    string2 = lines[n+1]
    string3 = lines[n+2]
    for i in string1:
        for j in string2:
            for k in string3:
                if(i == j == k and i.isupper()):
                    sum_two = sum_two + ord(i) - 38
                    break
                if(i == j == k and i.islower()):
                    sum_two = sum_two + ord(i) - 96
                    break
            if(i == j == k):
                break
        if(i == j == k):
            break
print(sum_two)
