# Bubble Sort Algorithm
def bubble_sort(array):
    swap = True
    array_length = len(array)
    while(swap):
        swap = False
        for x in range(array_length-1):
            if array[x] > array[x+1]:
                array[x], array[x+1] = array[x+1], array[x]
                swap = True


# Selection Sort Algorithm
def selection_sort(array):
    for x in range(len(array)): 
        for i in range(x+1, len(array)):
            if array[x] > array[i]:
                array[x], array[i] = array[i], array[x]


# Insertion Sort Algorithm
def insertion_sort(array):
    array_length = len(array)
    for i in range(1, array_length):
        key = array[i]
        j = i - 1
        while (j >= 0) and (array[j] > key):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

# Shell Sort Algorithm
def shell_sort(array):
    hop = len(array) // 2
    while hop > 0:      
        array_length = len(array)
        for i in range(hop, array_length):
            key = array[i]
            j = i - hop
            while (j >= 0) and (array[j] > key):
                array[j+hop] = array[j]
                j -= hop
            array[j+hop] = key
        hop = hop // 2


# Iterative Version of Quick Sort Algorithm
def iterative_quick_sort(lst):  # Foi funcional em todos os tipos de listas usados, entretando, apresentou um alto tempo de execução em listas muito grandes
    stack = []
    stack.append(lst)

    result = []
    while stack:
        current_list = stack.pop()
        
        if len(current_list) == 0:
            continue
        elif len(current_list) == 1:
            result.insert(0, *current_list)
            continue

        pivot = current_list[0]

        smaller = [x for x in current_list[1:] if x <= pivot]
        greater = [x for x in current_list[1:] if x > pivot]

        stack.append(smaller)
        stack.append([pivot])
        stack.append(greater)

    lst = result
