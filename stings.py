import math
c=50
h=30

value=[]
item=[x for x in input().split(',')]

for d in item:
    value.append(str(int(round(math.sqrt((2*c*d)/h)))))

print(value)