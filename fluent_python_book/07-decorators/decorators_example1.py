def loggable(log_type='file'):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print('log to1:', log_type)
            result = func(*args, **kwargs)
            print('log to2:', log_type)
            return result

        return wrapper

    return my_decorator


@loggable(log_type='console')
def func1(arg1, *content, arg2, **attrs):
    print(locals())
    pass


func1(10, 'content', arg2='TEST', b='test')
