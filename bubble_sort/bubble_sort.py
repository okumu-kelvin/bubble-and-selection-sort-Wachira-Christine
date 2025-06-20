def bubble_sort(un_list):
    # TODO: Implement bubble sort
    n = len(un_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            #Swap elements found greater than the next element
            if un_list[j] > un_list[j + 1]:
                un_list[j], un_list[j + 1] = un_list[j+1], un_list[j]

    return un_list
