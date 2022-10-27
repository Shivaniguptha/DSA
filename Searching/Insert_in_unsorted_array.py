# Inserting an element at the end of unsorted array

arr=[1,5,8,3,67,2,55]
n=int(input('Enter an element that has to be inserted at the end of array: '))

arr.append(n)
print('{} is inserted and the final array is {}'.format(n,arr))
