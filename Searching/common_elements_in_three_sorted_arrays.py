# To find common elements in three sorted arrays

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
            return binary_search(arr,mid+1,right,num)
        else:
            return binary_search(arr,left,mid-1,num)
    else:
        return -1

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
flag=0
l=[]

for i in arr1:
    z=binary_search(arr2,0,len(arr2)-1,i)
    if z!=-1:
        y=binary_search(arr3,0,len(arr3)-1,i)
        if y!=-1:
            flag=1
            l.append(i)

if flag==0:
    print('No common elements found')
else:
    print(l)
