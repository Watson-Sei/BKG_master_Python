import random
arr=[]
for i in range(10):
    arr.append(random.randint(1,100))

print(arr)


def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i]
                change = True
    return arr

bubble_sort(arr)
print(arr)