import random
import string
import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort


def generate_random_numbers(size):
    return [random.randint(0, 1000) for _ in range(size)]


def generate_random_str(size, length=8):
    return [
        "".join(random.choices(string.ascii_letters, k=length)) for _ in range(size)
    ]


def mesure_time(sort_func, data):
    start = timeit.default_timer()
    sort_func(data.copy())
    end = timeit.default_timer()
    return end - start


def timsort(arr):
    return sorted(arr)


def compare_sortings():
    sizes = [100, 1000, 10000]

    for size in sizes:
        print(
            f"Merge sort,Type: Numbers, Size: {size}, time {mesure_time(merge_sort, generate_random_numbers(size))}"
        )
        print(
            f"Inserting sort,Type: Numbers, Size: {size}, time {mesure_time(insertion_sort, generate_random_numbers(size))}"
        )
        print(
            f"Timsort,Type: Numbers, Size: {size}, time {mesure_time(timsort, generate_random_numbers(size))}"
        )
        print()
        print(
            f"Merge sort,Type: Str, Size: {size}, time {mesure_time(merge_sort, generate_random_str(size))}"
        )
        print(
            f"Inserting sort,Type: Str, Size: {size}, time {mesure_time(insertion_sort, generate_random_str(size))}"
        )
        print(
            f"Timsort,Type: Str, Size: {size}, time {mesure_time(timsort, generate_random_str(size))}"
        )


if __name__ == "__main__":
    compare_sortings()
