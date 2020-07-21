import math
x = int(input())
y = int(input())
if y < 2:
    print(round(math.log(x), 2))
else:
    print(round(math.log(x, y), 2))
