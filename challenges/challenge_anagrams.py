def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + equal + quick_sort(right)


def is_anagram(first_string, second_string):
    first_lower = first_string.lower()
    second_lower = second_string.lower()

    sorted_string_first = ''.join(quick_sort(list(first_lower)))
    sorted_string_second = ''.join(quick_sort(list(second_lower)))

    is_anagram = False
    if first_lower != "" and second_lower != "":
        if sorted_string_first == sorted_string_second:
            is_anagram = True

    return sorted_string_first, sorted_string_second, is_anagram

    raise NotImplementedError
