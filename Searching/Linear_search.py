# Initializing array and item that has to be seached.

arr=[1,2,6,8,4,3]
item=8
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
