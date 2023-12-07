import functools
from typing import Any


def how_are_you(func):
    @functools.wraps(func)
    def wrapped_func() -> Any:
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        return func()

    return wrapped_func

@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()