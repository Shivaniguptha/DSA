# To find which elements in the second array are missing from the first array.

def missingNumbers(arr, brr):
    result=set()
    for i in brr:
        if i in arr:
            arr.remove(i)
        else:
            result.add(int(i))
    result=list(result)
    result=sorted(result)
    for i in result:
        print(int(i),end=' ')

arr=[1,2,3,4,5,6]
brr=[1,2,2,3,3,3,4,5,6,8,9,0]
missingNumbers(arr,brr)
