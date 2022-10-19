# To print the array of elements using recursion

def array(l,i):
    length=len(l)
    if length==i:
        return
    else:
        print(l[i])
        array(l,i=i+1)

i=0
arr=[1,2,3,4]
array(arr,i)
