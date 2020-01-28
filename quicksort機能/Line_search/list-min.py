import random
x = []
for i in range(10):
    x.append(random.randint(1,100))
print(x)


minval = x[0]
for i in range(0,len(x),1):
    print(i)
    if x[i] < minval:
        minval = x[i]

print("最小値:",minval)