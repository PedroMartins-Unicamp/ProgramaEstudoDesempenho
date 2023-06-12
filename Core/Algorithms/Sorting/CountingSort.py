def counting_sort(lst):
    length = len(lst)
    count = [0] * (length+1)  # length+1 is a bit more performatic than max(lst)+1, in case of using a different list pattern, consider changing the code
    output = [0] * length

    for i in range(0, length):
        count[lst[i]] += 1

    for j in range(1, length+1): # length+1 --- max(lst)+1
        count[j] += count[j-1]

    a = length-1
    while a >= 0:
        output[count[lst[a]]-1] = lst[a]
        count[lst[a]] -= 1
        a -= 1

    for k in range(0, length):
        lst[k] = output[k]
