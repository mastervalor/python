import random

def shuttle(arr):
    random.shuffle(arr)
    return arr

print(shuttle([3, 4, 'ef', False]))

def skyline(arr):
    new_arr =[]
    for i in range(len(arr)):
        if arr[i] > 0 and i == 0:
            new_arr.append(arr[i])
        if arr[i] > arr[i-1]:
            new_arr.append(arr[i])
    return new_arr

print(skyline([-1,1,1,7,3]))
print(skyline([1,3,5,4]))