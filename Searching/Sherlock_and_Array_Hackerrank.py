# To find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.
# If it meets this criteria then it returns YES. Otherwise, return NO.

def balancedSums(arr):
    for i in range(0,len(arr)):
        sum1=sum(arr[:i])
        sum2=sum(arr[i+1:])
        #print(sum1,sum2)
        if sum1==sum2:
            return 'YES'
    return "NO"

arr=[5,6,8,11]
result=balancedSums(arr)
print(result)
