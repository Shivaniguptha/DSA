# this is a function which return the index of required item.

def binarysearch(arr, n, k):
    left=0
    right=n-1
    while right>=left:
        mid=int(left+((right-left)/2))
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            left=mid+1
        else:
            right=mid+1

# array and the number (k) are already intialized here. ANd n means length of the array
            
arr=[1,2,3,4,5]
k=4
n=5
print(binarysearch(arr,n,k))
