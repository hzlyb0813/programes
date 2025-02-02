import random
yuan = 0
fang = 0
x = 0
y = 0
rr = 0
xy = 0
for counter in range(1,10000000001):
    x = random.random()*100
    y = random.random()*100
    rr = 10000
    xy = x*x+y*y
    if xy<rr:
        yuan = yuan+1
    else:
        fang = fang+1
yf = yuan+fang        
print(4*yuan/yf)                       