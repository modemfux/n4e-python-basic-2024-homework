# Набор констант, импортируемых для использования внутри функций

MAC_NOTATIONS_DICT = {
    "IEEE EUI-48": ("-", 5, False),
    "IEEE EUI-48 lowercase": ("-", 5, True),
    "UNIX": (":", 5, True),
    "cisco": (":", 2, True),
    "bare": ("", 13, True),
}

NORMALIZE_INTF_DICT = {
    "Eth": "Ethernet",
    "Fa": "FastEthernet",
    "Gig": "GigabitEthernet",
    "GE": "GigabitEthernet",
    "Ten": "TenGigabitEthernet",
    "TE": "TenGigabitEthernet",
    "XGE": "TenGigabitEthernet",
}
