from hw_data import MAC_NOTATIONS_DICT

# ## Task1: Нотация МАС адреса

# В задании на циклы [Task1](/998.hw.tasks/020.loops.md#task1-цикл-for) было
# реализовано определение нотации МАС адреса для списка МАС адресов.
# Нужно модифицировать этот код с ипользованием функции. При этом функция
# должна принимать один МАС адрес (строка) и возвращать его нотацию (строка).
# Затем с помощью этой функции напечатать нотацию для МАС адресов
# из списка `mac_list`.

# mac_list = [
#     "50-46-5D-6E-8C-20",
#     "50-46-5d-6e-8c-20",
#     "50:46:5d:6e:8c:20",
#     "5046:5d6e:8c20",
#     "50465d6e8c20",
#     "50465d:6e8c20",
# ]


def get_mac_notation(mac: str) -> str:
    notation = "Unknown notation"
    for key, value in MAC_NOTATIONS_DICT.items():
        sep = value[0]
        check = (
            sep,
            mac.count(sep),
            mac.islower(),
        )
        found = bool(value == check)
        if found:
            notation = key
    return notation


if __name__ == "__main__":
    mac_list = [
        "50-46-5D-6E-8C-20",
        "50-46-5d-6e-8c-20",
        "50:46:5d:6e:8c:20",
        "5046:5d6e:8c20",
        "50465d6e8c20",
        "50465d:6e8c20",
    ]
    for mac in mac_list:
        print(f"MAC {mac} is {get_mac_notation(mac)}")
