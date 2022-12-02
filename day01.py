with open("inputs/day01_input.txt") as file:
    lines = [line.rstrip() for line in file]
max_cal = [0,0,0]
tmp_cal = 0
count = 0
for line in lines:
    if(line):
        tmp_cal = tmp_cal + int(line)
        #print(tmp_cal)
    else:
        if(tmp_cal > min(max_cal)):
            index_min = min(range(len(max_cal)), key=max_cal.__getitem__)
            max_cal[index_min] = tmp_cal
            count = count + 1
            #if(count == 2):
            #    break
        tmp_cal = 0
print(max_cal)
print(count)

sum = 0
for i in max_cal:
    sum = sum + i
print(sum)
  
