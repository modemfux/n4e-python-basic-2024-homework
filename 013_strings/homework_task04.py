# Task4: Форматирование строк
# Task4.1: Простейший шаблон
# Сделать из текста
#
# #
# bridge-domain 555
#  vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
#  vxlan vni 10555
#  #
#  evpn
#   route-distinguisher 192.168.43.34:10555
#   vpn-target 64512:10555 export-extcommunity
#   vpn-target 64512:10555 import-extcommunity
#  arp broadcast-suppress enable
# #
# шаблон со следующими входными параметрами (название переменной
# / описание / пример значения в шаблоне)
#
# bd_id / bridge domain id / 555
# intf_start / первый интерфейс / 10GE1/0/1
# intf_end / последний интерфейс / 10GE1/0/48
# rid / router id / 192.168.43.34
# bgp_as / номер bgp as / 64512
# Последние два байта в rd/rt и значение vxlan vni и формируются
# присоединением слева символа 1 (один) к значению bd_id.
# Если длина bd_id меньше 4 символов, то перед конкатенацией с 1
# нужно bd_id дополнить нулями слева до 4 символов.
# Например (bd_id > result) 555 > 10555, 2345 > 12345, 4 > 10004
#
# Восстановить исходный текст из шаблона, передав в него необходимые параметры:
#
# template = <ваш код тут>
#
# config = <ваш код тут, со значениями:
#     bd_id=555,
#     intf_start=10GE1/0/1,
#     intf_end=10GE1/0/48,
#     rid=192.168.43.34,
#     bgp_as=64512,
# >
# Получить конфигурацию для еще двух наборов параметров
# (меняем только bd_id, остальные можно оставить без изменений)
# и убедиться, что rd/rt/vni формируются без ошибок
#
# bd_id = 2541. Ожидаем в vni/rt/rf - 12541
# bd_id = 84. Ожидаем в vni/rt/rf - 10084

template = """#
bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni 1{bd_id:04}
 #
 evpn
  route-distinguisher {rid}:1{bd_id:04}
  vpn-target {bgp_as}:1{bd_id:04} export-extcommunity
  vpn-target {bgp_as}:1{bd_id:04} import-extcommunity
 arp broadcast-suppress enable
#
"""

print("Task4.1 Variant 1:")
config = template.format(
    bd_id=555,
    intf_start="10GE1/0/1",
    intf_end="10GE1/0/48",
    rid="192.168.43.34",
    bgp_as=64512,
)
print(config)

print("Task4.1 Variant 2:")
config = template.format(
    bd_id=2541,
    intf_start="10GE1/0/1",
    intf_end="10GE1/0/48",
    rid="192.168.43.34",
    bgp_as=64512,
)
print(config)

print("Task4.1 Variant 3:")
config = template.format(
    bd_id=84,
    intf_start="10GE1/0/1",
    intf_end="10GE1/0/48",
    rid="192.168.43.34",
    bgp_as=64512,
)
print(config, end="\n" * 2)

# Task4.2: Преобразование в двоичную систему - 1
# Сделать преобразование в двоичную систему без использования
# функции bin() трех чисел:
#
# 42
# 32
# 255

task_42_1 = "{:b}".format(42)
task_42_2 = f"{32:b}"
task_42_3 = f"{255:b}"

print("Task 4.2:")
print(f"42 in bin: {task_42_1}")
print(f"32 in bin: {task_42_2}")
print(f"255 in bin: {task_42_3}", end="\n" * 2)

# Task4.3: Преобразование в двоичную систему - 2
# Сделать преобразование в двоичную систему без использования функции bin()
# трех чисел (42/32/255 из прошлого задания), дополнив при этом количество
# бит до 8 нулями слева (11 -> 00001011).

task_43_1 = "{:08b}".format(42)
task_43_2 = f"{32:08b}"
task_43_3 = f"{255:08b}"

print("Task 4.3:")
print(f"42 in bin: {task_43_1}")
print(f"32 in bin: {task_43_2}")
print(f"255 in bin: {task_43_3}", end="\n" * 2)

# Task4.4: Преобразование в двоичную систему - 3
# Получить полное двоичное представление ip адреса (т.е. без разделения
# на октеты): 10.23.43.234 -> 00001010000101110010101111101010.

print("Task 4.4:")
ip = "10.23.43.234"
oct1, oct2, oct3, oct4 = ip.split(".")
result = f"{int(oct1):08b}{int(oct2):08b}{int(oct3):08b}{int(oct4):08b}"
print("IP:", ip)
print(f"Length: {len(result)}")
print("Binary IP:", result, end="\n" * 2)

# Task4.5: RTP запись
# Сформировать RTP запись для адреса "77.88.55.242"
# -> "242.55.88.77.in-addr.arpa"

print("Task 4.5:")
ip = "77.88.55.242"
ip_list = ip.split(".")
ptr = ".".join(ip_list[::-1]) + ".in-addr.arpa"
print("IP:", ip)
print("PTR:", ptr, end="\n" * 2)

# Task4.5: Доработка задания по числам
# Доработать задание по числам таким образом, что бы на вход
# можно было подавать строку вида "ip / mask". В конце распечатать
# 5 искомых параметров (network, wildcard, broadcast,
# min_host_ip, max_host_ip).

ip = "192.168.43.54 / 255.255.254.0"

ip_addr, mask = ip.split("/")
ip_addr = ip_addr.strip()
mask = mask.strip()

ip1, ip2, ip3, ip4 = ip_addr.split(".")
m1, m2, m3, m4 = mask.split(".")

net1 = int(ip1) & int(m1)
net2 = int(ip2) & int(m2)
net3 = int(ip3) & int(m3)
net4 = int(ip4) & int(m4)

wc1 = ~int(m1) & 255
wc2 = ~int(m2) & 255
wc3 = ~int(m3) & 255
wc4 = ~int(m4) & 255

bc1 = net1 + wc1
bc2 = net2 + wc2
bc3 = net3 + wc3
bc4 = net4 + wc4

ip_template = "{}.{}.{}.{}"

network = ip_template.format(net1, net2, net3, net4)
wildcard = ip_template.format(wc1, wc2, wc3, wc4)
broadcast = ip_template.format(bc1, bc2, bc3, bc4)
min_host_ip = ip_template.format(net1, net2, net3, net4 + 1)
max_host_ip = ip_template.format(bc1, bc2, bc3, bc4 - 1)

print("Task 4.5:")
print("Network:", network)
print("Wildcard:", wildcard)
print("Broadcast:", broadcast)
print("Min host IP:", min_host_ip)
print("Max host IP:", max_host_ip, end="\n" * 2)

# Task4.6: Удаление символов в строке

output = """
Local Interface         Exptime(s) Neighbor Interface            Neighbor Device
-------------------------------------------------------------------------------------
100GE1/0/1                    107  100GE1/0/1                    spine1.pod1.stg
10GE1/0/1                     105  10GE1/0/1                     test-server.stg
""".strip()

result1 = output.replace("\r\n", "\n").replace("-\n", "").replace("-", "")
print("Task 4.6 variant 1: with replace")
print(result1, end="\n" * 2)

mid_list = output.replace("\r\n", "\n").split("\n")
result_list = mid_list[0:1] + mid_list[2:]
result2 = "\n".join(result_list)

print("Task 4.6 variant 2: with split and lists")
print(result2, end="\n" * 2)

# Task4.7: Нормализация имен интерфейсов
# Даны имена интерфейсов в коротком виде (Eth0/1, GE1/0/2, Тen4/3).
# Произвести преобразование коротких имен в полные
#
# Eth0/1 -> Ethernet0/1
# GE1/0/2 -> GigabitEthernet1/0/2
# Тen4/3 -> TenGigabitEthernet4/3

if_name1 = "Eth0/1"
if_name2 = "GE1/0/2"
if_name3 = "Тen4/3"

# Т кириллицей в Ten - это опечатка? Или специально :)?

if_name1 = if_name1.replace("Eth", "Ethernet")
if_name2 = if_name2.replace("GE", "GigabitEthernet")
if_name3 = if_name3.replace("Тen", "TenGigabitEthernet")

print("Task 4.7:")
print("Normalized if_name1:", if_name1)
print("Normalized if_name2:", if_name2)
print("Normalized if_name3:", if_name3)
