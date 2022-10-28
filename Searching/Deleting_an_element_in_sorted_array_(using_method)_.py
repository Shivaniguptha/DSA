# Deleting an element in sorted array

arr=[1,2,3,4,5]
num=int(input('Enter a number that has to be deleted from the array: '))

arr.remove(num)

print('{} is deleted from array and the final array is {}'.format(num,arr))
