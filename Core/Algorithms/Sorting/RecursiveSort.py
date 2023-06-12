# Merge Sort Algorithm 
def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if (end - start) > 1:
        middle = (end + start) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle, end)
        __merge(array, start, middle, end)

def __merge(array, start, middle, end):
    left_list = array[start: middle]
    right_list = array[middle: end]
    top_left, top_right = 0, 0
    for k in range(start, end):
        if top_left >= len(left_list):
            array[k] = right_list[top_right]
            top_right += 1
        elif top_right >= len(right_list):
            array[k] = left_list[top_left]
            top_left += 1
        elif left_list[top_left] < right_list[top_right]:
            array[k] = left_list[top_left]
            top_left += 1
        else: 
            array[k] = right_list[top_right]
            top_right += 1


# Quick Sort Algorithm
def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array)-1
    if start < end:
        pivot = __partitionate(array, start, end)
        quick_sort(array, start, pivot-1)
        quick_sort(array, pivot+1, end)


def __partitionate(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i

# def semiiterativequicksort(a, lo=0, hi=None):
#     if hi == None:
#         hi = len(a) - 1
#     while(hi - lo > 0):
#         pivot = a[hi]
#         i = lo
#         for j in range(lo, hi):
#             if a[j] <= pivot:
#                 a[i],a[j] = a[j],a[i]
#                 i += 1
#         a[i],a[hi] = a[hi],a[i]
#         if(i - lo <= hi - i):
#             semiiterativequicksort(a, lo, i-1)
#             lo = i+1
#         else:
#             semiiterativequicksort(a, i+1, hi)
#             hi = i-1
