# Bubble Sort

def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr=[2,5,1,11,7,20]
bubble_sort(arr)
print('sorted array is', arr)
