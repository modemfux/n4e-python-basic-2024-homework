from time import perf_counter, sleep

# ## Task3: Замыкания

# На встрече одним из примеров использования замыкания был таймер
#
# from time import perf_counter
#
# def timer():
#     start = perf_counter()
#     def inner():
#         print(f"{perf_counter() - start:.2f}")
#     return inner
#
# t = timer()
#
# t()
# # >>> 2.75
#
# t()
# # >>> 5.19
#
# При каждом вызове `t()` происходит печать количества секунд, прошедших с
# момента вызова `t = timer()`. Нужно модифицировать код таким образом,
# что бы показывалось время, прошедшее с последнего вызова `t()`, т.е.
# считать секунды между вызовами `t()`.


def timer():
    call = perf_counter()

    def inner():
        nonlocal call
        now = perf_counter()
        result = now - call
        print(f"{result:.2f}")
        call = now

    return inner


if __name__ == "__main__":
    tick = timer()
    for i in range(1, 5):
        tick()
        tick()
        sleep(i)
        tick()
