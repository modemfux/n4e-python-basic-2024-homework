from textwrap import dedent

# Task1: Многострочный текст

# Записать текст конфигурации в переменную config.
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

print("Task1.1: Переменная определелена глобально")

config = """#
bridge-domain 555
 vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
 vxlan vni 10555
 #
 evpn
  route-distinguisher 192.168.43.34:10555
  vpn-target 64512:10555 export-extcommunity
  vpn-target 64512:10555 import-extcommunity
 arp broadcast-suppress enable
#
"""

print(config)
print("=" * 30)

print("Task1.2: Переменная определена внутри блока")
print("Вариант 1:")

if True:
    config = """#
bridge-domain 555
 vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
 vxlan vni 10555
 #
 evpn
  route-distinguisher 192.168.43.34:10555
  vpn-target 64512:10555 export-extcommunity
  vpn-target 64512:10555 import-extcommunity
 arp broadcast-suppress enable
#
"""
print(config)

print("Вариант 2:")

if True:
    config = """
    #
    bridge-domain 555
     vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48
     vxlan vni 10555
     #
     evpn
      route-distinguisher 192.168.43.34:10555
      vpn-target 64512:10555 export-extcommunity
      vpn-target 64512:10555 import-extcommunity
     arp broadcast-suppress enable
    #"""

print(dedent(config))

print("Вариант 3:")

if True:
    config = (
        "#\n"
        "bridge-domain 555\n"
        " vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48\n"
        " vxlan vni 10555\n"
        " #\n"
        " evpn\n"
        "  route-distinguisher 192.168.43.34:10555\n"
        "  vpn-target 64512:10555 export-extcommunity\n"
        "  vpn-target 64512:10555 import-extcommunity\n"
        " arp broadcast-suppress enable\n"
        "#\n"
    )

print(config)
