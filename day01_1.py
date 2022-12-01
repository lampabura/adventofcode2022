with open("day01_input.txt") as file:
    lines = file.readline()
    max_cal = 0
    for line in lines:
        tmp_cal = 0
        if(line):
            tmp_cal = tmp_cal + int(line)
        else:
            if(tmp_cal > max_cal):
                max_cal = tmp_cal
                tmp_cal = 0
  
