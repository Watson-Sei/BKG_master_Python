import random
x = []
for i in range(10):
    x.append(random.randint(1,100))
print(x)

maxval = x[0]
for i in range(0,len(x),1):
    if x[i] > maxval:
        maxval = x[i]

print("最大値",maxval)