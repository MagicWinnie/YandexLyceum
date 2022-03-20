def good_dreams(text, first_divisor, second_divisor, *args, **kwargs):
    arr = text.split(first_divisor)
    arr = list(map(lambda x: x.split(second_divisor), arr))
    for func, ind in args:
        if func not in kwargs:
            continue
        arr[ind] = list(map(kwargs[func], arr[ind]))
    return arr
