# ## Task6: Sorted
#
# Встроенная функция `sorted` принимает последовательность на вход, и
# возвращает сортированный вариант этой последовательности:
#
# ```python
# seq = [4, 2, 90, 12]
#
# sorted(seq)
# # >>> [2, 4, 12, 90]
# ```
#
# Если требуется сортировать словарь, то его нужно сначала превратить в
# последовательность (`dict.items` возвращает последовательность из кортежей,
# в которой каждый кортеж это пара ключ-значение), а затем отсортировать эту
# последовательность кортежей, и в конце обратно собрать в словарь.
#
# ```python
# d = {1: "c", 3: "a", 2: "b"}
#
# d.items()
# dict_items([(1, 'c'), (3, 'a'), (2, 'b')])
#
# dict(sorted(d.items()))
# # >>> {1: 'c', 2: 'b', 3: 'a'}
# ```
#
# По умолчанию сортировка идет по ключу (первый элемент каждого из кортежа).
# Если нужно сортировать по значению (или какой-то другой логике), то можно
# использовать параметр `key`, в который передать ссылку на функцию, которая
# вернет элемент, по которому нужно сортировать:
#
# ```python
# d = {1: "c", 3: "a", 2: "b"}
# d.items()
# dict_items([(1, 'c'), (3, 'a'), (2, 'b')])
#
# # lambda item: item[1] - item = кортеж (ключ, значение) - параметр lambda
# функции, возвращаем item[1], т.е. значение словаря, именно по этим данным
# из каждого кортежа будет сортировка
#
# dict(sorted(d.items(), key=lambda item: item[1]))
# # >>> {3: 'a', 2: 'b', 1: 'c'}
# ```
#
# Есть словарь устройств. Применение функций `sorted` сортирует словарь по
# имени устройств:
#
# ```python
# devices = {
#     "rt3": {
#         "nb_id": 32,
#         "ip": "3.3.3.3",
#     },
#     "rt1": {
#         "nb_id": 908,
#         "ip": "1.1.1.1",
#     },
#     "sw2": {
#         "nb_id": 5233,
#         "ip": "2.2.2.2",
#     },
# }
#
# dict(sorted(devices.items()))
#
# # {'rt1': {'nb_id': 908, 'ip': '1.1.1.1'},
# #  'rt3': {'nb_id': 32, 'ip': '3.3.3.3'},
# #  'sw2': {'nb_id': 5233, 'ip': '2.2.2.2'}}
# ```
#
# Нужно добавить `key` таким образом, что бы сортировка была по `nb_id`:
#
# ```python
# dict(sorted(devices.items(), key=<ваша lambda функция>))
#
# # {'rt3': {'nb_id': 32, 'ip': '3.3.3.3'},
# #  'rt1': {'nb_id': 908, 'ip': '1.1.1.1'},
# #  'sw2': {'nb_id': 5233, 'ip': '2.2.2.2'}}
# ```
#

if __name__ == "__main__":

    devices = {
        "rt3": {
            "nb_id": 32,
            "ip": "3.3.3.3",
        },
        "rt1": {
            "nb_id": 908,
            "ip": "1.1.1.1",
        },
        "sw2": {
            "nb_id": 5233,
            "ip": "2.2.2.2",
        },
    }

    print(dict(sorted(devices.items(), key=lambda x: x[1].get("nb_id"))))