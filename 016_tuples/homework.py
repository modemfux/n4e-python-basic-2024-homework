from collections import deque, namedtuple

# Task 1: Удаление элементов
# Есть список
#
# intf_list = ["gi0/0", "gi0/1",
#              "gi0/22", "gi0/23",
#              "gi0/3", "gi0/4"]
# Нужно преобразовть к вот такому виду:
# ["gi0/0", "gi0/1", "gi0/2",
#  "gi0/3", "gi0/4"]
# (gi0/22, gi0/23 лишние элементы, gi0/2 не хватает)

intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]

print("Task 1 variant 1 (pop and insert):")
intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]
intf_list.pop(intf_list.index("gi0/22"))
intf_list.pop(intf_list.index("gi0/23"))
intf_list.insert(intf_list.index("gi0/1") + 1, "gi0/2")
print(intf_list, end="\n\n")

print("Task 1 variant 2 (remove, append and sort):")
intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]
intf_list.remove("gi0/22")
intf_list.remove("gi0/23")
intf_list.append("gi0/2")
intf_list.sort()
print(intf_list, end="\n\n")

print("=" * 80, end="\n" * 2)
# Task 2: Добавление элементов

# Есть список
# intf_list = ["gi0/1"]
# Добавить слева к нему элемент "gi0/0", справа - "gi0/2"

print("Task 2 variant 1 (via insert and append):")
intf_list = ["gi0/1"]
intf_list.insert(0, "gi0/0")
intf_list.append("gi0/2")
print(intf_list, end="\n\n")

print("Task 2 variant 2 (via deque):")
intf_list = deque(["gi0/1"])
intf_list.appendleft("gi0/0")
intf_list.append("gi0/2")
intf_list = list(intf_list)
print(intf_list, end="\n\n")

print("=" * 80, end="\n" * 2)

# Task 3: Список списков

# Есть матрица
#
# mtx = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# Получить два листа, в которых будут элементы диагоналей матрицы:
#
# diag1
# >>> [1, 5, 9]
#
# diag2
# >>> [3, 5, 7]

print("Task 3:")

mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

diag1 = [mtx[0][0], mtx[1][1], mtx[2][2]]
diag2 = [mtx[0][2], mtx[1][1], mtx[2][0]]
print(f"diag1 = {diag1}")
print(f"diag2 = {diag2}")

print("=" * 80, end="\n" * 2)

# Task 4: Преобразование строки

# Есть входная строка
#
# output = "switchport trunk allowed vlan 2,101,104"
# Нужно получить список vlan (типа int).
#
# vlans
# >>> [2, 101, 104]

print("Task 4 variant 1 (via slice and map):")
output = "switchport trunk allowed vlan 2,101,104"
vlan_list = output.split(" ")[-1].split(",")
vlan_list = list(map(int, vlan_list))
print(vlan_list)

print("Task 4 variant 2 (via unpacking):")
output = "switchport trunk allowed vlan 2,101,104"
*_, vlan_list = output.split(" ")
vlan1, vlan2, vlan3 = vlan_list.split(",")
vlan_list = [int(vlan1), int(vlan2), int(vlan3)]
print(vlan_list)

print("=" * 80, end="\n" * 2)

# Task 5: Namedtuple
#
# Дан вывод
#
# output = """
# Interface             IP-Address      OK?    Method Status      Protocol
# GigabitEthernet0/2    192.168.190.235 YES    unset  up          up
# GigabitEthernet0/4    192.168.191.2   YES    unset  up          down
# TenGigabitEthernet2/1 unassigned      YES    unset  up          up
# Te36/45               unassigned      YES    unset  down        down
# """.strip()
# Создать namedtuple InterfaceStatus и сделать список intf_brief = <...>
# из 4ех элементов типа InterfaceStatus, в каждом из котором будет разобранные
# из соответсвующей строки входных данных (заголовок пропускаем,
# он не нужен, только данные по интерфейсам).
#
# isinstance(intf_brief, list)
# >>> True
#
# len(intf_brief)
# >>> 4
#
# intf_brief[0].name
# >>> 'GigabitEthernet0/2'
#
# intf_brief[0].ip
# >>> '192.168.190.235'
#
# intf_brief[0].status
# >>> 'up'

print("Task 5:")

output = """
Interface             IP-Address      OK?    Method Status      Protocol
GigabitEthernet0/2    192.168.190.235 YES    unset  up          up
GigabitEthernet0/4    192.168.191.2   YES    unset  up          down
TenGigabitEthernet2/1 unassigned      YES    unset  up          up
Te36/45               unassigned      YES    unset  down        down
""".strip().replace(
    "\r\n", "\n"
)

f_names, *interfaces = output.split("\n")
f_names = f_names.replace("-", "_").replace("?", "").lower().split()
intf1, intf2, intf3, intf4 = interfaces

InterfaceStatus = namedtuple(typename="InterfaceStatus", field_names=f_names)
result = [
    InterfaceStatus(*intf1.split()),
    InterfaceStatus(*intf2.split()),
    InterfaceStatus(*intf3.split()),
    InterfaceStatus(*intf4.split()),
]

print(f"Type of result: {type(result)}")
print(f"Length of result: {len(result)}")
print(f"Interface {result[0].interface} IP: {result[0].ip_address}")
print(f"Interface {result[1].interface} OK: {result[1].ok}")
print(f"Interface {result[2].interface} Status: {result[2].status}")
print(f"Interface {result[3].interface} Protocol: {result[3].protocol}")
print(f"Interface {result[0].interface} Method: {result[0].method}")

print("=" * 80, end="\n" * 2)
