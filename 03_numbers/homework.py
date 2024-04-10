# Reverse


def _not(number):
    return 255 - number


# 192.168.43.54 / 255.255.254.0

ip1 = 192
ip2 = 168
ip3 = 43
ip4 = 54

mask1 = 255
mask2 = 255
mask3 = 254
mask4 = 0

net1 = ip1 & mask1
net2 = ip2 & mask2
net3 = ip3 & mask3
net4 = ip4 & mask4

wc1 = _not(mask1)
wc2 = _not(mask2)
wc3 = _not(mask3)
wc4 = _not(mask4)

bc1 = net1 + wc1
bc2 = net2 + wc2
bc3 = net3 + wc3
bc4 = net4 + wc4

network = str(net1) + "." + str(net2) + "." + str(net3) + "." + str(net4)
wildcard = str(wc1) + "." + str(wc2) + "." + str(wc3) + "." + str(wc4)
broadcast = str(bc1) + "." + str(bc2) + "." + str(bc3) + "." + str(bc4)
# fmt: off
min_host_ip = (str(net1) + "." + str(net2)
               + "." + str(net3) + "." + str(net4 + 1))
max_host_ip = (str(bc1) + "." + str(bc2)
               + "." + str(bc3) + "." + str(bc4 - 1))
# fmt: on

print("Network:", network)
print("Wildcard:", wildcard)
print("Broadcast:", broadcast)
print("Min host IP:", min_host_ip)
print("Max host IP:", max_host_ip)
print("")

# 192.168.43.54 / 255.255.255.240

ip1 = 192
ip2 = 168
ip3 = 43
ip4 = 54

mask1 = 255
mask2 = 255
mask3 = 255
mask4 = 240

net1 = ip1 & mask1
net2 = ip2 & mask2
net3 = ip3 & mask3
net4 = ip4 & mask4

wc1 = _not(mask1)
wc2 = _not(mask2)
wc3 = _not(mask3)
wc4 = _not(mask4)

bc1 = net1 + wc1
bc2 = net2 + wc2
bc3 = net3 + wc3
bc4 = net4 + wc4

network = str(net1) + "." + str(net2) + "." + str(net3) + "." + str(net4)
wildcard = str(wc1) + "." + str(wc2) + "." + str(wc3) + "." + str(wc4)
broadcast = str(bc1) + "." + str(bc2) + "." + str(bc3) + "." + str(bc4)
# fmt: off
min_host_ip = (str(net1) + "." + str(net2)
               + "." + str(net3) + "." + str(net4 + 1))
max_host_ip = (str(bc1) + "." + str(bc2)
               + "." + str(bc3) + "." + str(bc4 - 1))
# fmt: on

print("Network:", network)
print("Wildcard:", wildcard)
print("Broadcast:", broadcast)
print("Min host IP:", min_host_ip)
print("Max host IP:", max_host_ip)
print("")
