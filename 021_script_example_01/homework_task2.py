from collections import namedtuple


# ## Task2: LLDP - description check
#
# Есть вывод lldp сосдей на устройстве:
#
# ```python
# # display lldp neighbor brief
# lldp_output = """
# GE1/0/1          br1.hq            GE0/0/5             107
# GE1/0/2          br2.hq            GE0/0/5             92
# GE1/0/3          sw1.hq            GE1/0/47            98
# XGE1/0/1         sw2.hq            GE1/0/51            93
# GE2/0/2          br2.hq            GE0/0/6             112
# GE2/0/3          sw12.hq           GE1/0/48            98
# XGE2/0/1         sw2.hq            GE1/0/52            93
# """.strip()
# ```
#
# и вывод описаний на интерфейсах
#
# ```python
# # display interface description
# description_output = """
# GigabitEthernet1/0/1        up      up       br1.hq.net.ru
# GigabitEthernet1/0/2        up      up       br2.hq.net.ru
# GigabitEthernet1/0/3        up      up       sw1.hq.net.ru
# GigabitEthernet2/0/1        up      up       br1.hq.net.ru
# GigabitEthernet2/0/2        up      up       br2.hq.net.ru
# GigabitEthernet2/0/3        up      up       sw1.hq.net.ru
# XGigabitEthernet1/0/1       up      up       sw2.hq.net.ru
# XGigabitEthernet2/0/1       up      up       sw2.hq.net.ru
# """.strip()
# ```

# Нужно сравнить описание на интерфейсе и lldp
# соседа (если он есть есть) и если описание не совпадает
# с информацией по lldp, то написать об этом (считаем, что
# sw1.hq и sw1.hq.net.ru это одно и тоже устройство, просто
# в описании записан домен)

NORM_DICT = {"GE": "GigabitEthernet", "XGE": "XGigabitEthernet"}


def normalize_intf_name(intf: str) -> str:
    for short, norm in NORM_DICT.items():
        if intf.startswith(short):
            return intf.replace(short, norm)
    return intf


def normalize_hostname_by_domain(hostname: str, domain: str) -> str:
    if not domain.startswith("."):
        domain = "." + domain
    if hostname.endswith(domain):
        return hostname[: len(hostname) - len(domain)]
    return hostname


def get_lldp_dict(lldp_out: str) -> dict:

    lldp_headers = ["own_intf", "nbr_name", "nbr_intf"]
    LLDPNbrs = namedtuple(typename="LLDPNbrs", field_names=lldp_headers)

    lldp_dict = {}

    for line in lldp_out.splitlines():
        own_intf, nbr_name, nbr_intf, *_ = line.split()
        own_intf = normalize_intf_name(own_intf)
        nbr_intf = normalize_intf_name(nbr_intf)
        neighbor = LLDPNbrs(own_intf, nbr_name, nbr_intf)
        lldp_dict.setdefault(own_intf, []).append(neighbor)

    return lldp_dict


def get_desc_dict(desc_out: str) -> dict:
    desc_headers = ["intf", "desc"]
    Description = namedtuple(typename="Description", field_names=desc_headers)
    desc_dict = {}

    for line in desc_out.splitlines():
        intf, _, _, desc = line.strip().split()
        intf = normalize_intf_name(intf)
        desc_dict[intf] = Description(intf, desc)

    return desc_dict


def compare_lldp_with_description(
    lldp_dict: dict, desc_dict: dict, domain: str
) -> tuple:
    wrong_desc = set()
    no_desc = set()
    for intf, nbrs in lldp_dict.items():
        if not desc_dict.get(intf):
            no_desc.add(intf)
        else:
            for nbr in nbrs:
                lldp_name = normalize_hostname_by_domain(nbr.nbr_name, domain)
                desc_name = normalize_hostname_by_domain(
                    desc_dict.get(intf).desc, domain
                )
                if not lldp_name == desc_name:
                    wrong_desc.add((intf, desc_name))
    return wrong_desc, no_desc


def generate_report(
    lldp_output: str, desc_output: str, domain=".net.ru", silent=False
) -> tuple:
    lldp_dict = get_lldp_dict(lldp_output)
    desc_dict = get_desc_dict(desc_output)
    wrong_desc, no_desc = compare_lldp_with_description(
        lldp_dict,
        desc_dict,
        domain,
    )
    if not silent and wrong_desc:
        for intf, desc in wrong_desc:
            print(f"Wrong description on {intf}. Should be {desc + domain}.")
        print("")
    if not silent and no_desc:
        for intf in no_desc:
            print(f"There is no description on {intf}")
        print("")
    return wrong_desc, no_desc


if __name__ == "__main__":
    lldp_output = """
GE1/0/1          br1.hq            GE0/0/5             107
GE1/0/2          br2.hq            GE0/0/5             92
GE1/0/3          sw1.hq            GE1/0/47            98
XGE1/0/1         sw2.hq            GE1/0/51            93
GE2/0/2          br2.hq            GE0/0/6             112
GE2/0/3          sw12.hq           GE1/0/48            98
XGE2/0/1         sw2.hq            GE1/0/52            93
XGE2/0/5         br11.hq           XGE2/0/5            11
""".strip()

    description_output = """
GigabitEthernet1/0/1        up      up       br1.hq.net.ru
GigabitEthernet1/0/2        up      up       br2.hq.net.ru
GigabitEthernet1/0/3        up      up       sw1.hq.net.ru
GigabitEthernet2/0/1        up      up       br1.hq.net.ru
GigabitEthernet2/0/2        up      up       br2.hq.net.ru
GigabitEthernet2/0/3        up      up       sw1.hq.net.ru
XGigabitEthernet1/0/1       up      up       sw2.hq.net.ru
XGigabitEthernet2/0/1       up      up       sw2.hq.net.ru
""".strip()

    generate_report(lldp_output, description_output)
