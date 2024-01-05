#program to implement insertion sort

#function executing insertion sort
def insertion_sort(arr,n):
    for i in range(1,n):                 #looping from one to n,through the unsorted sublist
        temp = arr[i]                    #storing arr[i] in a temperory variable 
        j = i-1                          #declaring unsorted sublist index from j-1
        while(j>=0 and arr[j]>temp):     #loop while index of unsorted sublist greater than zero and temp is less than corresponding item
            arr[j+1] = arr[j]            #swap
            j -= 1                       #decrement j
        arr[j+1] = temp                  #temp variable assigned to a[j+1]
    return arr                           #returning array
arr = [22,1,78,5,4,10,1,6,2]
n = len(arr) 
result = insertion_sort(arr,n)
print(result)