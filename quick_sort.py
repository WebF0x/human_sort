def quick_sort(things, fun_is_smaller):
    if len(things) <= 1:
        return things
    pivot_index = len(things) // 2
    pivot_value = things[pivot_index]
    smallers = [x for i, x in enumerate(things) if i is not pivot_index and fun_is_smaller(x, pivot_value)]
    biggers = [x for i, x in enumerate(things) if i is not pivot_index and x not in smallers]
    return quick_sort(smallers, fun_is_smaller) + [pivot_value] + quick_sort(biggers, fun_is_smaller)
