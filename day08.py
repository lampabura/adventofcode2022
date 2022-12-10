import numpy as np

trees = []
vis = 0

row = 0
col = 0

def scene_count(i,j):
    u = 0
    for k in np.flip(trees[:i,j]):
        if(k < trees[i,j]):
            u = u + 1
        elif(k >= trees[i,j]):
            u = u + 1
            break
        else:
            break
    d = 0
    for l in trees[i+1:,j]:
        if(l < trees[i,j]):
            d = d + 1
        elif(l >= trees[i,j]):
            d = d + 1
            break
        else:
            break
    l = 0
    for m in np.flip(trees[i,:j]):
        if(m < trees[i,j]):
            l = l + 1
        elif(m >= trees[i,j]):
            l = l + 1
            break
        else:
            break
    r = 0
    for n in trees[i,j+1:]:
        if(n < trees[i,j]):
            r = r + 1
        elif(n >= trees[i,j]):
            r = r + 1
            break
        else:
            break
    return u*d*l*r

with open("inputs/day08_input.txt") as file:
    lines = [line.rstrip() for line in file]

for i,line in enumerate(lines):
    trees.append(list(map(int,line)))
    col = i+1
row = len(trees[0])
trees = np.array(trees)
#scene = np.zeros(shape=(row,col))
max_scene = 0

for i in range(row):
    for j in range(col):
        if( trees[i,j] > np.max(trees[:i,j],initial=-1) or
            trees[i,j] > np.max(trees[i+1:,j],initial=-1) or
            trees[i,j] > np.max(trees[i,:j],initial=-1) or
            trees[i,j] > np.max(trees[i,j+1:],initial=-1) ):
            vis = vis + 1
        if(scene_count(i,j) > max_scene):
            max_scene = scene_count(i,j)

print(vis)
print(max_scene)
        


