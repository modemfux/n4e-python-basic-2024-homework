# ## Task7: Параметры функции
#
# Нужно написать функцию, которая принимает три ключевых параметра (строго
# ключевых, позиционные не принимает). Второй и третий параметр должны быть
# опциональными, со значением по умолчанию `None`. Функция должна печатать
# значения переданных аргументов, если они не равны `None`.
#
# ```python
# def foo(<сигнатура вашей функции>):
#     <тело вашей функции>
#
# foo(var1=32)
# # var1 = 32
#
# foo(var1=32, var3="test")
# # var1 = 32
# # var3 = test
# ```
#


def key_func(*, var1, var2=None, var3=None):
    result_list = []
    for var in var1, var2, var3:
        print(var)
        result_list.append(var)
    return result_list


if __name__ == "__main__":
    sample1 = {"var1": "Only one"}
    sample2 = {"var1": "First", "var3": "Third"}
    sample3 = {"var1": "First", "var2": "Second", "var3": "Third"}
    sample4 = (1, 2, 3)

    for sample in sample1, sample2, sample3:
        print("=" * 10 + f"Sample {sample}")
        key_func(**sample)
        print("=" * 80)

    try:
        print("=" * 10 + f"Sample {sample4}")
        key_func(*sample4)
    except Exception as error:
        print(f"Sample {sample4} caused exception:")
        print(error)
