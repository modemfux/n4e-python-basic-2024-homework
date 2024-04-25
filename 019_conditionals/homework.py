# Условия (if)
# Task1: Определение нотации MAC
# Существуют несколько нотаций предствления MAC адреса, например:
#
# IEEE EUI-48: 50-46-5D-6E-8C-20
# IEEE EUI-48 lowercase: 50-46-5d-6e-8c-20
# UNIX: 50:46:5d:6e:8c:20
# cisco: 5046:5d6e:8c20
# bare: 50465d6e8c20
# Нужно написать код, который определяет тип нотации адреса
# из перечисленных выше.
#
# Входные данные: строка, содержащая MAC адрес.
#
# 50-46-5D-6E-8C-20
# 50-46-5d-6e-8c-20
# 50:46:5d:6e:8c:20
# 5046:5d6e:8c20
# 50465d6e8c20
# 50465d:6e8c20
# Результат: напечатанный тип нотации. Если определить не удалось - напечать
# нотация для 50465d:6e8c20 неизвестна (это для последнего примера)
#
# mac = "50-46-5D-6E-8C-20"
#
# <...код...>
#     mac_notation = <...>
#
# print(f"нотация {mac}: {mac_notation}")
# >>> 'нотация 50-46-5D-6E-8C-20: IEEE EUI-48'

MID_END = "\n" + "-" * 12 + "\n"
TASK_END = "=" * 80 + "\n"

print("Task1: Определение нотации MAC", end=MID_END)

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

# Task2: Определение класса ip адреса
# Есть переменная с ip адресом (строка), нужно опрделить класс (A/B/C/D/E)
# ip адреса.
#
# ip = "10.3.2.1"
#
# <...код...>
#     ip_class = >...>
#
# print(f"класс ip {ip}: {ip_class}")
# "класс ip 10.3.2.1: A"

print("Task2: Определение класса ip адреса", end=MID_END)

ip_list = [
    "10.3.2.1",
    "172.16.0.1",
    "192.168.1.1",
    "224.1.2.3",
    "241.3.2.1",
    "256.256.256.256",
    "A.B.C.D",
    "17.13.2456",
]

for ip in ip_list:
    ip_class = ""
    splitted = ip.split(".")
    all_numeric = all(map(lambda x: x.isnumeric(), splitted))
    if len(splitted) == 4 and all_numeric:
        oct_ = int(splitted[0])
        if oct_ in range(0, 128):
            ip_class = "A"
        elif oct_ in range(128, 192):
            ip_class = "B"
        elif oct_ in range(192, 224):
            ip_class = "C"
        elif oct_ in range(224, 240):
            ip_class = "D"
        elif oct_ in range(240, 256):
            ip_class = "E"
    if ip_class:
        print(f"{ip}: Class {ip_class}", end=MID_END)
    else:
        print(f"{ip}: Wrong IP format", end=MID_END)

print(TASK_END)

# Task3: Использование dict вместо if
# Есть два шаблона интерфейсов
#
# access = """
# interface {if_name}
#    switchport mode access
#    switchport access vlan {vlan}
# !
# """.strip()
#
# trunk = """
# interface {if_name}
#    switchport mode trunk
#    switchport trunk allowed vlan {vlan}
# !
# """.strip()
# Есть два словаря с параметрами интерфейсов:
#
# intf1 = {
#     "if_name": "gi0/1",
#     "vlan": 102,
#     "mode": "access",
# }
#
# intf2 = {
#     "if_name": "gi0/2",
#     "vlan": 103,
#     "mode": "trunk",
# }
# Нужно подставить параметры интерфейсов в соответсвующие шаблоны и получить
# конфигурацию обоих интерфейсов (тип интерфейса задается по ключу mode)
# двумя способами:
#
# с использованием условий (т.е. с if)
# без использования условий (без if)
# print(intf1_config)
# >>>
# interface gi0/1
#    switchport mode access
#    switchport access vlan 102
# !
#
# print(intf2_config)
# >>>
# interface gi0/2
#    switchport mode trunk
#    switchport trunk allowed vlan 103
# !

print("Task3: Использование dict вместо if", end=MID_END)

access = """
interface {if_name}
   switchport mode access
   switchport access vlan {vlan}
!
""".strip()

trunk = """
interface {if_name}
   switchport mode trunk
   switchport trunk allowed vlan {vlan}
!
""".strip()

intf1 = {
    "if_name": "gi0/1",
    "vlan": 102,
    "mode": "access",
}

intf2 = {
    "if_name": "gi0/2",
    "vlan": 103,
    "mode": "trunk",
}

print("Variant 1: via If", end=MID_END)

for intf in (intf1, intf2):
    if intf["mode"] == "access":
        print(access.format(**intf), end=MID_END)
    elif intf["mode"] == "trunk":
        print(trunk.format(**intf), end=MID_END)

print()

print("Variant 2: via dict", end=MID_END)
config_dict = {"access": access, "trunk": trunk}
for intf in (intf1, intf2):
    print(config_dict.get(intf.get("mode", "")).format(**intf), end=MID_END)

print(TASK_END)
