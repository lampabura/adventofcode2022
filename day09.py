# ......
# ......
# ......
# ......
# s..... (s: starting point as reference)

def move_T(H,T):
    r_off = H.real-T.real
    i_off = H.imag-T.imag
    if(abs(r_off) <= 1 and
       abs(i_off) <= 1):
       return T
    
    else:
        if(r_off > 0): T = T + 1
        elif(r_off < 0): T = T-1 

        if(i_off > 0): T = T + 1j
        elif(i_off < 0): T = T-1j

    return T


T = []
knots = 10
for i in range(knots):
    T.append(0+0j)
visited = []

with open("inputs/day09_input.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    dir, l = line.split()
    for i  in range(int(l)):
        if(dir == 'U'):
            T[0] = T[0] + 1j
        elif(dir == 'D'):
            T[0] = T[0] - 1j
        elif(dir == 'R'):
            T[0] = T[0] + 1
        elif(dir == 'L'):
            T[0] = T[0] - 1

        for i in range(1,knots):
            T[i] = move_T(T[i-1],T[i])
        if(T[9] not in visited):
            visited.append(T[9])

#print(visited)
print(len(visited))