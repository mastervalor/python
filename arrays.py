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


def zipit(arr1, arr2):
    longest_arr = arr1 if len(arr1)> len(arr2) else arr2
    new_arr = []
    for i in range(len(longest_arr)):
        if i <= (len(arr1))-1:
            new_arr.append(arr1[i])
        if i <= (len(arr2))-1:
            new_arr.append(arr2[i])
    return new_arr

print(zipit([4,15,100],[10,20,30,40]))