def quickSort(a,left,right):
    if left < right:
        pivot = partition(a,left,right)
        quickSort(a,left,pivot-1)
        quickSort(a,pivot+1,right)
        
def partition(a,left,right):
    pivot = left
    while left < right:
        while a[left] <= a[pivot] and left < pivot:
            left += 1
        while a[right] > a[pivot]:
            right -= 1
        if left < right:
            a[left],a[right] = a[right], a[left]
            
    a[pivot],a[right] = a[right],a[pivot]
    return pivot

a = []
n = int(input("Enter the no. of elements: "))
print(f"Enter the {n} elements: ")
for i in range(n):
    a.append(input())
quickSort(a,0,n-1)
print("The sorted order is : ")
for i in range(n):
    print(a[i])