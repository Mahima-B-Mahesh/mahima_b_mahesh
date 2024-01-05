#proogram to implement selection sort

def selection_sort(arr,n):
    for i in range(n-1):                                #loops through the unsorted list
        min = i                                         #set min = i = 0
        for j in range(i+1,n):                          #loop to find the min element 
            if arr[j]<arr[min]:
                min = j
        if min != i:
            arr[i],arr[min]=arr[min],arr[i]
    return arr

arr = [7,4,10,8,3,1]

n = len(arr)

result = selection_sort(arr,n)

print(result)