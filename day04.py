# decorator
import time

def time_decorator(func):
    def wrraper(*arg):
        start_num = time.time()
        result = func(*arg)
        end_time = time.time()
        stop_watch = (end_time-start_num)
        print(f"걸린 시간은 {stop_watch}초 입니다")
        return result
    return wrraper

@time_decorator
def description_decorator(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r

    return inner


def squares(n):
    """
    제곱 함수
    """
    return n * n

@description_decorator
def power(b, e):
    """
    거듭제곱 함수
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result

f1 = time_decorator(description_decorator(power))
print(f1(2, 3))

f2 = time_decorator((description_decorator(squares)))
print(f2(3))

f3 = squares(3)
print(f3)

f4 = (pow(2,3))
print(f4)