# Insertion Sort

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j>=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = temp

arr=[2,5,1,11,7,20]
insertion_sort(arr)
print('sorted array is', arr)
