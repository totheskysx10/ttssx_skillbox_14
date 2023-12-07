import functools
import time
from typing import Any


def sleep(func):
    @functools.wraps(func)
    def wrapped_func() -> Any:
        time.sleep(2)
        return func()

    return wrapped_func

@sleep
def test():
    print('<Тут что-то происходит...>')


test()