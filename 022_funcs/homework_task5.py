# ## Task5: Filter vs list comprehension
#
# Для фильтрации элементов последовательности можно использовать list
# comprehension. Например, отфильтруем только "rt" устройства в
# последовательности `["rt1", "RT2", "SW1", "sw2"]`:
#
# ```python
# seq = ["rt1", "RT2", "SW1", "sw2"]
#
# [elem for elem in seq if elem.lower().startswith("rt")]
# # >>> ['rt1', 'RT2']
# ```
#
# Аналогичный результат можно получить использую функцию `filter`: встроенная
# функция `filter` применяет другую функцию (передаем ссылку на нее в
# аргументах) к последовательности, что бы понять, нужно ли сохранять очередной
#  элемент последовательности или нет (на основе True/False - результата
# выполнения переданной в аргументах функции):
#
# ```python
# seq = ["rt1", "RT2", "SW1", "sw2"]
#
# list(filter(str.islower, seq))
# ['rt1', 'sw2']
# ```
#
# В примере `str.islower` применяется к каждому элементу последовательности
# `seq`, если элемент в нижнем регистре (`str.islower` возвращает `True` в
# этом случае), то он остается в отфильтрованной последовательности, в
# противном случае (`False`) он пропускается.
#
# Нужно заменить `str.islower` на `lamdba` функцию, что бы выражение оставляло
# в последовательности только "rt" устройства:
#
# ```python
# seq = ["rt1", "RT2", "SW1", "sw2"]
#
# list(filter(<ваша lambda функция>, seq))
# ['rt1', 'RT2']
# ```
#


if __name__ == "__main__":
    seq = ["rt1", "RT2", "SW1", "sw2"]
    result = list(filter(lambda x: str(x).lower().startswith("rt"), seq))
    print(result)
