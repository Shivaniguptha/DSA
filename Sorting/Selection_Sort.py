# Selection Sort

def selection_sort(arr):
    for i in range(0,len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr=[2,5,1,11,7,20]
selection_sort(arr)
print('sorted array is', arr)
