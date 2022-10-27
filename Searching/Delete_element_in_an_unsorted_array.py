# Deleting an element in unsorted array

arr=[1,5,8,3]
num=int(input('Enter a number that has to be deleted from the array: '))

for i in range(0,len(arr)-1):
    if arr[i]==num:
        arr.remove(arr[i])

print('{} is deleted from array and the final array is {}'.format(num,arr))
