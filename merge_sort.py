def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    merged = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged
