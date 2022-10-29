# Check if a pair exists with given sum in given array

def binary_search(arr,left,right,num):
    if right>left:
        mid=int(left+((right-left)/2))
        if arr[mid]==num:
            return int(mid)
        elif arr[left]==num:
            return int(left)
        elif arr[right]==num:
            return int(right)
        elif arr[mid]<num:
            return binary_search(arr,left,mid-1,num)
        else:
            return binary_search(arr,mid+1,right,num)
    else:
        return -1

arr=[5,3,1,4,2]
sum=7
flag=0

arr=sorted(arr)
for i in arr:
    y=sum-i
    z=binary_search(arr,0,len(arr)-1,y)
    if z!=-1:
        flag=1
        print('the two numbers are {}, {}'.format(i,y))

if flag==0:
    print('elements not found')
