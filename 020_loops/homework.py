from copy import deepcopy
from pprint import pprint


MID_END = "\n" + "-" * 12 + "\n"
TASK_END = "=" * 80 + "\n"


# ## Task1: Цикл `for`
#
# Используя данные задания [Определение нотации MAC]
# (/998.hw.tasks/019.conditionals.md#task1-определение-нотации-mac)
# поместить алгоритм определения в цикл и распечатать найденные
# нотации для следующего списка MAC адресов:
#
# ```python
# mac_list = [
#     "50-46-5D-6E-8C-20",
#     "50-46-5d-6e-8c-20",
#     "50:46:5d:6e:8c:20",
#     "5046:5d6e:8c20",
#     "50465d6e8c20",
#     "50465d:6e8c20",
# ]
#
# for <код>
# ```

print("Task1: Цикл `for`", end=MID_END)
mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]

notations_dict = {
    "IEEE EUI-48": ("-", 5, False),
    "IEEE EUI-48 lowercase": ("-", 5, True),
    "UNIX": (":", 5, True),
    "cisco": (":", 2, True),
    "bare": ("", 13, True),
}

for mac in mac_list:
    found = False
    notation = "Unknown notation"
    for key, value in notations_dict.items():
        sep, qty, capital = value
        check = (
            sep,
            mac.count(sep),
            mac.islower(),
        )
        found = bool(value == check)
        if found:
            notation = key
            break
    print(f"Notation for {mac} is '{notation}'", end=MID_END)
print(TASK_END)

# ## Task2: Составление списков
#
# Дан список hostname устройств
#
# ```python
# devices = [
#     "rt1.lan.hq.net",
#     "p1.mpls.hq.net",
#     "p2.mpls.hq.net",
#     "sw1.lan.hq.net",
#     "dsw1.lan.hq.net",
# ]
# ```
#
# Используя list comprehension получить из него список устройств lan
# домена (lan.hq.net)
#
# ```python
# ["rt1.lan.hq.net", "sw1.lan.hq.net", "dsw1.lan.hq.net"]
# ```

print("Task2: Составление списков", end=MID_END)

devices = [
    "rt1.lan.hq.net",
    "p1.mpls.hq.net",
    "p2.mpls.hq.net",
    "sw1.lan.hq.net",
    "dsw1.lan.hq.net",
]

domain = "lan.hq.net"
lan_devices = [device for device in devices if domain in device]
for device in lan_devices:
    print(f"Device {device} in domain {domain}", end=MID_END)

print(TASK_END)

# ## Task3: Составление словарей
#
# Есть шаблон подключения к оборудованию
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
# И список устройств:
#
# ```python
# hostnames = ["rt1", "rt2", "sw1", "sw2"]
# ```

print("Task3: Составление словарей", end=MID_END)

hostnames = ["rt1", "rt2", "sw1", "sw2"]
SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

# ### Task3.1: Цикл `for`
#
# Используя цикл `for` составить словарь `devices` вида
# `{hostname: scrapli_params, ...}`.
#
# ```python
# devices = {}
# for <код>
# ```

print("Task3.1: Цикл `for`", end=MID_END)
devices = {}

for host in hostnames:
    devices[host] = deepcopy(SCRAPLI_TEMPLATE)
pprint(devices)

print(TASK_END)

# ### Task3.2: Генератор словарей
#
# Используя генератор словарей составить словарь `devices` вида
# `{hostname: scrapli_params, ...}`.
#
# ```python
# devices = {<код>}
# ```

print("Task3.2: Генератор словарей", end=MID_END)
devices = {host: deepcopy(SCRAPLI_TEMPLATE) for host in hostnames}
pprint(devices)

print(TASK_END)

# ## Task4: Комбинация условий и циклов
#
# Дана строчка конфигурации
#
# ```python
# line = "switchport trunk allowed vlan 100,200,300-500,600
# ```
#
# Проверить, входит ли:
#
# - vlan 400
# - vlan 800
#
# в список разрешенных на trunk'е vlan.
#

print("Task4: Комбинация условий и циклов", end=MID_END)

line = "switchport trunk allowed vlan 100,200,300-500,600"
vlans = line.split()[-1].split(",")
for check_vlan in ["400", "800"]:
    permit = False
    for vlan in vlans:
        if "-" in vlan:
            st_vlan, end_vlan = vlan.split("-")
            if int(check_vlan) in range(int(st_vlan), int(end_vlan) + 1):
                permit = True
        elif check_vlan == vlan:
            permit = True
    print(f"Vlan {check_vlan} is allowed: {permit}", end=MID_END)

print(TASK_END)
