# Given an array arr[]. Find the maximum value of prefix sum which is also suffix sum for index i in arr[].

arr = [-1, 2, 3, 0, 3, 2, -1]

for i in range(0,len(arr)):
  
    # Prefix sum of arr[0..3] = Suffix sum of arr[3..6]
    
    if sum(arr[:i+1]) == sum(arr[i:]):
        print(sum(arr[:i+1]))
