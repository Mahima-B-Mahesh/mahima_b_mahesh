def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = 1
        if flag == 0:
            break
    return arr

arr = [2,5,1,11,7,15,20,16,6,8,5]

result = bubble_sort(arr)


print(result)