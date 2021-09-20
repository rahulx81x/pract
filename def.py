x = 5
y = [1,4,5,4,5]


def modify(element, array):
    element += 1
    if element in array:
       element = modify(element, array)
    return element


def improve(n, arr):
    temp = []
    for i in range(n):
        if arr[i] not in temp:
            temp.append(arr[i])
        else:
            arr[i] = modify(arr[i],arr)
    temp = 0
    for i in arr:
        temp += i
    print(arr)
    return temp


print(improve(x,y))
