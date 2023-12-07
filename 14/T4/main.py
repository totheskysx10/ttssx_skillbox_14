import functools


def counter(func):
    @functools.wraps(func)
    def wrapped_func():
        wrapped_func.count += 1
        print(f"Функция {func.__name__} вызвана {wrapped_func.count} раз")
        return func()

    wrapped_func.count = 0
    return wrapped_func

@counter
def test():
    print('<Тут что-то происходит...>')


test()
test()
test()
test()
test()
test()
test()
test()