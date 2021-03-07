from functools import wraps


def my_dec(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print('result')
        return func(*args, **kwargs)

    return inner_func


@my_dec
def sumt(a, b):
    return a + b


print(sumt(2, 3))
