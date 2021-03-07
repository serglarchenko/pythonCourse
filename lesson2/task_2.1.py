l = list()
l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]


def filter_list_for(mixed_list):
    ints_list = list()
    for i in mixed_list:
        if isinstance(i, int):
            ints_list.append(i)
        else:
            continue
    return print(ints_list)


def filter_list_comprehensions(mixed_list):
    return print([i for i in mixed_list if isinstance(i, int)])


def filter_lambda(mixed_list):
    """Used method type() in this subtask"""
    return print(list(filter(lambda i: type(i) == int, mixed_list)))


filter_list_for(l)
filter_list_comprehensions(l)
filter_lambda(l)
