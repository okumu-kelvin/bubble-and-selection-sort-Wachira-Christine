def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)

    for i in range(n):
        #finding the minimum element in the unsorted
        min_idx = i
        for j in range (i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #Swaping element that is found to be less than the first unsorted element
        arr[i], arr[min_idx]= arr[min_idx], arr[i]

    return arr
