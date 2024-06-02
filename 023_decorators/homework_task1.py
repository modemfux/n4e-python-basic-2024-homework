from functools import wraps
from time import perf_counter, sleep
from random import randint


# ## Task1: декоратор для проверки производительности функции
#
# Нужно написать декоратор, который принимаем один обязательный аргумент -
# число повторений, и делает вызов декорируемой функции указанное число раз.
# При этом измеряется время выполнения каждого вызова, и в результате
# вычисляется среднее время выполнения функции. Функция `get_url`
# дана для примера декорирования, может быть любой в вашей реализации.
#
# import requests
#
# def benchmark(repeat_count):
#     <код декоратора>
#
# @benchmark(10)
# def get_url(url):
#     result = requests.get(url)
#
# get_url('https://google.com')
# # >>> Среднее время выполнения: 0.50399с.
#


def benchmark(rep_count: int):
    def inner_benchmark(func):
        name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(rep_count):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()
                times.append(end - start)
            average_time = sum(times) / rep_count
            print(
                f"Average execution time of function '{name}'",
                f"is {average_time:.10f} seconds",
            )
            return result

        return wrapper

    return inner_benchmark


@benchmark(3)
def random_sleep():
    sleeptime = randint(1, 5)
    print("I'm drowzy...")
    for i in range(sleeptime + 1):
        print("Zzzzzz....")
        sleep(1)
    print("I'm awake!", end="\n\n")


if __name__ == "__main__":
    random_sleep()
