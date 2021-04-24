import functools
import time


def clock(func):
    '''
    简单计时装饰器
    1.
    :param func: 外部函数
    :return: 内部函数
    '''

    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        args_str = ','.join((repr(arg) for arg in args))
        print("[%0.8fs] %s(%s)-->%s" % (elapsed, func.__name__, args_str, result))
        return result

    return clocked


def clock_mature(func):
    """
    成熟计时装饰器
    :param func: 外部函数
    :return: 内部函数
    """
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        args_list = []
        if args:
            args_list.append(','.join((repr(arg) for arg in args)))
        if kwargs:
            pairs = ["%s=%r" % (k, v) for k, v in sorted(kwargs.items())]
            args_list.append(pairs)

        args_str = ','.join(args_list)
        print("[%0.8fs] %s(%s)-->%s" % (elapsed, func.__name__, args_str, result))
        return result

    return clocked
