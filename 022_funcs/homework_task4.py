from pprint import pprint


# ## Task4: Парсинг конфигурации в словарь
#
# Дана конфигурация устройства в переменной [config]
# (/021.script.example.01/021.main.py), нужно распарсить конфигурацию в
# словарь таким образом, что:
#
# - каждая глобальная команда является ключом словаря
# - все подчиненные команды (саб-команды) помещаются в список
# - все пробельные символы в начале/конце всех строк убираем
# - если подчиненных команд нет, то значением становится пустой список
# - служебные строки ("", "!", "building", "exit") игнорируем.
#
# пример:
#
# ```text
# config (передается в функцию)
# !
# spanning-tree pathcost method long
# !
# lldp run
# !
# interface FastEthernet0/1
#  switchport access vlan 10
#  switchport mode access
#  spanning-tree portfast edge
#  spanning-tree bpduguard enable
# !
# ```
#
# ```text
# result (возвращается из функции)
# {
#     "spanning-tree pathcost method long": [],
#     "lldp run": [],
#     "interface FastEthernet0/1": [
#         "switchport access vlan 10",
#         "switchport mode access",
#         "spanning-tree portfast edge",
#         "spanning-tree bpduguard enable",
#     ],
# }
# ```
#
# ```python
# config = """
# spanning-tree mode rapid-pvst
# spanning-tree logging
# spanning-tree extend system-id
# spanning-tree pathcost method long
# !
# lldp run
# !
# interface FastEthernet0/1
#  switchport access vlan 10
#  switchport mode access
#  spanning-tree portfast edge
#  spanning-tree bpduguard enable
# !
# interface FastEthernet0/2
#  switchport access vlan 11
#  switchport mode access
#  spanning-tree portfast edge
#  spanning-tree bpduguard enable
# !
# interface FastEthernet0/3
#  switchport access vlan 51
#  switchport mode access
#  spanning-tree portfast edge
#  spanning-tree bpduguard enable
# !
# interface FastEthernet0/4
#  switchport mode access
#  spanning-tree portfast edge
#  spanning-tree bpduguard enable
# !
# interface GigabitEthernet0/1
#  description mgmt1.core - FastEthernet0/32
#  switchport mode trunk
#  switchport trunk allowed vlan 10,20,30,40,50-70,80,90
#  mls qos trust cos
#  ip dhcp snooping trust
# !
# interface GigabitEthernet0/2
#  description mgmt2.core - FastEthernet0/32
#  switchport mode trunk
#  mls qos trust cos
#  ip dhcp snooping trust
# !
# interface GigabitEthernet0/3
#   description mgmt3.core - FastEthernet0/32
#   switchport mode trunk
#   switchport trunk allowed vlan 10,20,30,40,50-70,80,90
#   switchport trunk allowed vlan add 150,151
#   mls qos trust cos
#   ip dhcp snooping trust
# !
# interface GigabitEthernet0/4
#  description mgmt4.core - FastEthernet0/32
#  ip address 1.2.3.4 255.255.255.0
# !
# line vty 0 4
#  password cisco
# !
# """
#
# def parse_config(config):
#     result = {}
#     ...
#     return result
# ```
#


def get_config_dict(config: str) -> dict:
    result = {}
    for line in config.splitlines():
        if not line.startswith("!"):
            if not line.startswith(" "):
                key = line.strip()
                result[key] = []
            elif all([line != "", "building" not in line, "exit" not in line]):
                result[key].append(line.strip())
    return result


if __name__ == "__main__":
    config = """
spanning-tree mode rapid-pvst
spanning-tree logging
spanning-tree extend system-id
spanning-tree pathcost method long
!
lldp run
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/2
 switchport access vlan 11
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/3
 switchport access vlan 51
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/4
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface GigabitEthernet0/1
 description mgmt1.core - FastEthernet0/32
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50-70,80,90
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/2
 description mgmt2.core - FastEthernet0/32
 switchport mode trunk
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/3
  description mgmt3.core - FastEthernet0/32
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30,40,50-70,80,90
  switchport trunk allowed vlan add 150,151
  mls qos trust cos
  ip dhcp snooping trust
!
interface GigabitEthernet0/4
 description mgmt4.core - FastEthernet0/32
 ip address 1.2.3.4 255.255.255.0
!
line vty 0 4
 password cisco
!
""".strip()
    pprint(get_config_dict(config))
