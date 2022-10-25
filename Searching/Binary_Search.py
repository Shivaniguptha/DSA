# Binary search in python

def Binary_search(arr, left, right, item):

    if right>left:
        mid=int(left+((right-left)/2))
        
        if arr[mid]==item:
            return mid
        
        elif arr[mid]>item:
            return Binary_search(arr, left, mid-1, item)
        
        else:
            return Binary_search(arr, mid+1, right, item)

    else:
        return -1


arr=[10,20,30,40,50,60,70,80]
item=int(input('Enter the number that has to be searched: '))

result= Binary_search(arr, 0, len(arr)-1, item)

if result==-1:
    print('{} is not found in {}'.format(item, arr))

else:
    print('{} is found at the index {}'.format(item, result))
