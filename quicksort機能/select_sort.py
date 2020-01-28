import random
arr = []
for i in range(10):
    arr.append(random.randint(1,100))
print(arr)
print(min(arr))


def select_sort(arr):
    for i in range(len(arr)-1):
        min_value = min(arr[i+1:])
        print(min_value)
        min_index = arr.index(min_value)

        if arr[i] > min_value:
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

select_sort(arr)
print(arr)