# To Check if a pair exists with given sum in given array

arr = [0, -1, 2, -3, 1]
x= -2

for i in range(0,len(arr)):
    y=x-i
    if y in arr:
        print('the two numbers are {}, {}'.format(i,y))
