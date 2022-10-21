# Initializing array.

arr=[1,2,6,8,4,3]
item=int(input('Enter the value that has to be searched: '))
length=len(arr)
flag=0

# Linearly traverse the array using a for loop.

for i in range(0,length):
    if arr[i]==item:
        flag=1
        index=i
    
if flag==1:
    print('The index of required item is', index)
else:
    print('no index found')
