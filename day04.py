# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .23456...  2-6
# ...45678.  4-8

import re

fully_cont = 0
overlap = 0

with open("inputs/day04_input.txt") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    arr = re.split('-|,',line)
    arr = list(map(int, arr))
    if( (arr[0] <= arr[2] and arr[1] >= arr[3]) or
        (arr[0] >= arr[2] and arr[1] <= arr[3]) ):
        fully_cont = fully_cont + 1
    if( (arr[0] >= arr[2] and arr[0] <= arr[3]) or
        (arr[1] >= arr[2] and arr[1] <= arr[3]) or
        (arr[2] >= arr[0] and arr[2] <= arr[1]) or
        (arr[3] >= arr[0] and arr[3] <= arr[1]) ):
        overlap = overlap + 1
print(fully_cont)
print(overlap)
