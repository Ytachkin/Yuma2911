"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools


# this decorator makes it possible to get the data .__doc, .__name and information about the id of the function.
# it does not add anything to the function, but only reads its data and stores
def decorator(original_func):
    def indecorator(func):
        func.__original_func = original_func
        func.__doc__ = original_func.__doc__
        func.__name__ = original_func.__name__
        return func

    return indecorator


# in the new decorator, seted the previous decorator.
# This is a normal decorator that prints the return value of the passed function.
def print_result(func):
    @decorator(original_func=func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    # print comment of format """text""" inside function
    print(custom_sum.__doc__)
    # print function name
    print(custom_sum.__name__)
    # print information about id
    print(custom_sum.__original_func)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)