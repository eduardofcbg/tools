from functools import wraps


def tupled(func):
    @wraps(func)
    def wrapped(arg_tuple, kwarg_dict=None):
        kwarg_dict = kwarg_dict or {}
        return func(*arg_tuple, **kwarg_dict)

    return wrapped


def untupled(func):
    @wraps(func)
    def wrapped(*args):
        return func(args)

    return wrapped


def call_opt(func, x):
    return func(x) if x is not None else x
