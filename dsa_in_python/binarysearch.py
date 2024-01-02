def binary_search(arr,left,right,x):
    if right >= left:
        mid = left + (right - left)//2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,left,mid-1,x)
        else:
            return binary_search(arr,mid+1,right,x)
    else:
        return -1


arr = [10,20,30,40,50,60,70,80]
x = 40
result = binary_search(arr,0,len(arr)-1,x)

if result == -1:
    print(f"item {x} not found")
else:
    print(f"item {x} is present at index {result}")