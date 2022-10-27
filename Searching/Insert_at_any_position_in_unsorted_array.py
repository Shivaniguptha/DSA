# Inserting an element at any position in unsorted array

arr=[1,5,8,3]
num=int(input('Enter an element that has to be inserted at the end of array: '))
index=int(input('Enter the position to place the number: '))

arr1=[]
for i in range(0,index):
    arr1.append(arr[i])
arr1.append(num)
for i in range(index,len(arr)):
    arr1.append(arr[i])

print('{} is inserted and the final array is {}'.format(num,arr1))
