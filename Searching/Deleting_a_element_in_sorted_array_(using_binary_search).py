# Deleting an element in sorted array

def delete_num(arr,num):
    pos=binary_search(arr,0,len(arr)-1,num)
    if pos=='-1':
        print('element not found')
    for i in range(pos,len(arr)-1):
        arr[i]=arr[i+1]
    return 0

def binary_search(arr,left,right,num):
    if right>left:
        mid=int(left+((right-left)/2))
        if arr[mid]==num:
            return int(mid)
        elif arr[mid]>num:
            return binary_search(arr,left,mid-1,num)
        else:
            return binary_search(arr,mid+1,right,num)

arr=[1,2,3,4,5]
num=int(input('Enter a number that has to be deleted from the array: '))

delete_num(arr,num)

print('{} is deleted from array and the final array is {}'.format(num,arr[:-1]))
