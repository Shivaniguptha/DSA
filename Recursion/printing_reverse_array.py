# To print the array of elements in reverse order using recursion

def array(arr,n,i):
    if n==i:
        return
    else:
        print(arr[n-1])
        array(arr,n-1,i)

arr=[1,2,3,4]
n=len(arr)
i=0
array(arr,n,i)

