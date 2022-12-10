# noop
# addx 3
# addx -5
# 
# during cyc : val
# (0         :  1)
# noop
#  1         :  1
# addx 3
#  2         :  1
#  3         :  1
# addx -5
#  4         :  4
#  5         :  4
#  6         : -1


with open("inputs/day10_input.txt") as file:
    lines = [line.rstrip() for line in file]

crt = [[],[],[],[],[],[],[]]

x = [1]
res = 0

for line in lines:
    if(line == "noop"):
        x.append(x[-1])
    else:
        op,val = line.split()
        for i in range(1):
            x.append(x[-1])
        n = x[-1] + int(val)
        x.append(n)

for i in range(20,221,40):
    res += x[i-1] * i
print(res)

for i,val in enumerate(x):
    row = i // 40
    vis = "."
    spr = [val-1, val, val+1]
    j = i-(row*40)
    if(j in spr):
        vis = "#"
    crt[row] += vis

print("".join(str(i) for i in crt[0]))
print("".join(str(i) for i in crt[1]))
print("".join(str(i) for i in crt[2]))
print("".join(str(i) for i in crt[3]))
print("".join(str(i) for i in crt[4]))
print("".join(str(i) for i in crt[5]))





