def insertion_sort(lst:list):
    n = len(lst)
    if n <= 1: 
        return

    for i in (range(1,n)):
        tmp = lst[i]

        j = i-1
        while j>=0 and lst[j] > tmp:
            lst[j+1] = lst[j]
            j-=1
        lst[j+1] = tmp
    return lst
