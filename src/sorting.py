

def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr
