from pprint import pprint

# Task1: Плоский словарь
#
# Создать два словаря c параметрами оборудования
# (ниже перечисление в виде "ключ = значение")
#
# - первый словарь (`device1`):
#   - hostname = r1.abcd.net
#   - ip = 192.168.1.1
#   - username = cisco
#   - password = secret
#   - platform = cisco_ios
#   - enable = True
# - второй словарь (`device2`):
#   - hostname = sw1.abcd.net
#   - ip = 192.168.1.2
#   - username = admin
#   - password = secret
#   - platform = huawei_vrp
#   - enable = False
#
# ```python
# device1 = <код>
#
# device2 = <код>
# ```

print("Task1: Плоский словарь")
device1 = {
    "hostname": "r1.abcd.net",
    "ip": "192.168.1.1",
    "username": "cisco",
    "password": "secret",
    "platform": "cisco_ios",
    "enable": True,
}

keys = ["hostname", "ip", "username", "password", "platform", "enable"]
dev2_values = [
    "sw1.abcd.net",
    "192.168.1.2",
    "admin",
    "secret",
    "huawei_vrp",
    False,
]
device2 = dict(zip(keys, dev2_values))

print("Device1 is:")
print("-" * 20)
pprint(device1)
print("Device2 is:")
print("-" * 20)
pprint(device2)

print("=" * 60, end="\n" * 2)

# Task2: Список словарей
#
# Создать список `devices_list`, содержащий словари `device1` и
# `device2` из задания [Task1](017.dicts.md#task1-плоский-словарь)
#
# ```python
# devices_list = <код>
# ```
#
# И добавить в него третье устройство с параметрами
#
# - hostname = wlc.abcd.net
# - ip = 192.168.1.3
# - username = wlc_admin
# - password = password
# - enable = False

print("Task2: Список словарей")

dev3_values = [
    "wlc.abcd.net",
    "192.168.1.3",
    "wlc_admin",
    "password",
    "",
    False,
]

devices_list = [device1, device2]
devices_list.append(dict(zip(keys, dev3_values)))
print("device_list is:")
print("-" * 20)
pprint(devices_list)
print("=" * 60, end="\n" * 2)

# Task3: Вложенный словарь (словарь словарей)
#
# На основе списка из [Task2](017.dicts.md#task2-список-словарей) создать
# словарь `devices_dict` в котором в качестве ключей будут выступать
# `hostname` устройств, а в качестве значений - соответсвующие
# элементы списка `devices_list`.
#
# ```python
# {
#     "r1.abcd.net": {
#         "hostname": "r1.abcd.net",
#         "ip": "192.168.1.1",
#         ...
#     },
#     "sw1.abcd.net": {
#         "hostname": "sw1.abcd.net",
#         "ip": "192.168.1.2",
#         ...
#     }
# }
# ```

print("Task3: Вложенный словарь (словарь словарей):")

devices_dict = {
    devices_list[0]["hostname"]: devices_list[0],
    devices_list[1]["hostname"]: devices_list[1],
    devices_list[2]["hostname"]: devices_list[2],
}

print("devices_dict is:")
print("-" * 20)
pprint(devices_dict)
print("=" * 60, end="\n" * 2)

# Task4: Обновление словаря
#
# Есть базовая заготовка (шаблон)
#
# ```python
# SCRAPLI_TEMPLATE = {
#     "auth_username": "cisco",
#     "auth_password": "password",
#     "transport": "system",
#     "auth_strict_key": False,
#     "port": 22,
# }
# ```
#
# Создать список из двух словарей на основе шаблона
# `SCRAPLI_TEMPLATE` дополнив/обновив
# его парами ключ = значение (сам шаблон при этом меняться не должен)
#
# - для первого словаря
#   - hostname = sw1.abcd.net
# - для второго словаря
#   - hostname = sw1.abcd.net
#   - transport = telnet
#   - port = 23
#

print("Task4: Обновление словаря:")

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

# fmt: off
scrapli_list = [
    SCRAPLI_TEMPLATE | {"hostname": "sw1.abcd.net"},
    SCRAPLI_TEMPLATE | {"hostname": "sw1.abcd.net",
                        "transport": "telnet",
                        "port": 23},
]
# fmt: on

print("scrapli_list is:")
print("-" * 20)
pprint(scrapli_list)
print("SCRAPLI_TEMPLATE after generating list:")
print("-" * 20)
pprint(SCRAPLI_TEMPLATE)
print("=" * 60, end="\n" * 2)
