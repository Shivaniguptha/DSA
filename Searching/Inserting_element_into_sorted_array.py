# Inserting an element in sorted array

arr=[1,2,4,5,6]
num=int(input('Enter a number that has to be inserted to the array: '))
arr1=[]

for i in range(0,len(arr)-1):
    arr1.append(arr[i])
    if arr[i]<num and num<arr[i+1]:
        arr1.append(num)
    
print('{} is inserted to an array and the final array is {}'.format(num,arr1))
