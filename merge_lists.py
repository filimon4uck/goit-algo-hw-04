from merge_sort import merge


def merge_k_lists(lists: list):
    if not lists:
        return []
    while len(lists) > 1:
        merged_list = []
        for i in range(0, len(lists), 2):
            left = lists[i]
            right = lists[i + 1] if i + 1 < len(lists) else []
            print("Left", left)
            print("Right", right)
            merged_list.append(merge(left, right))
            print("Merged list", merged_list)
        lists = merged_list

    return lists[0]


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
