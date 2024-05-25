from hw_data import NORMALIZE_INTF_DICT

# ## Task2: Нормализация имени интерфейса

# В задании [Task4.8](/998.hw.tasks/013.strings.md#task48-нормализация-имен-
# интерфейсов) делали нормализацию имени интерфейса (Eth -> Ethernet, GE ->
# GigabitEthernet, Тen -> TenGigabitEthernet). Нужно написать функцию, которая
# принимает имя интерфейса (строка, например "Eth0/3") и возвращает его
# нормализованное имя (строка, например "Ethernet0/3").

# Распечатать нормализованные имена интерфейсов для следующих входных данных:

# interfaces = [
#     "Eth0/0",
#     "Gig0/4/3",
#     "GE4/4",
#     "Po3",
#     "Ten5/4",
#     "XGE4/1",
#     "Eth-Trunk4",
# ]
#
# Правила преобразования:
#
# - Eth0/0 -> Ethernet0/0
# - Fa0/0 -> FastEthernet0/0
# - Gig0/0 -> GigabitEthernet0/0
# - GE0/0 -> GigabitEthernet0/0
# - Ten0/0 -> TenGigabitEthernet0/0
# - TE0/0 -> TenGigabitEthernet0/0
# - XGE0/0 -> TenGigabitEthernet0/0
#
# если входные данные не подходят ни под одно из условий, то возвращаем
# имя интерфейса без модификации: Loopback0 -> Loopback0.


def normalize_intf_name(intf: str) -> str:
    for short, norm in NORMALIZE_INTF_DICT.items():
        if intf.startswith(short) and len(intf) < 9:
            return intf.replace(short, norm)
    return intf


if __name__ == "__main__":
    interfaces = [
        "Eth0/0",
        "Gig0/4/3",
        "GE4/4",
        "Po3",
        "Ten5/4",
        "XGE4/1",
        "Eth-Trunk4",
    ]

    for interface in interfaces:
        line = f"{interface} is {normalize_intf_name(interface)}"
        print(line)
