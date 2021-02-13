"""
GitHub link
"""


def get_ip_from_raw_address(raw_address: str) -> str:
    pass


def get_network_address_from_raw_address(raw_address: str) -> str:
    pass


def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    pass


def get_binary_mask_from_raw_address(raw_address: str) -> str:
    pass


def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    pass


def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    pass


def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    pass


def get_ip_class_from_raw_address(raw_address: str) -> str:
    pass


def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    pass


# IP адреси - розробити функцію get_ip_from_raw_address(raw_address)
# адреси мережі - розробити функцію get_network_address_from_raw_address(raw_address)
# широкомовної адреси мережі - розробити функцію get_broadcast_address_from_raw_address(raw_address)
# маска підмережі у бінарній формі - розробити функцію get_binary_mask_from_raw_address(raw_address)
# першої можливої адреси вузла у даній мережі - розробити функцію get_first_usable_ip_address_from_raw_address(raw_address)
# передостанньої можливої адреси вузла у даній мережі - розробити функцію get_penultimate_usable_ip_address_from_raw_address(raw_address)
# загальної кількість можливих до алокації (використання) адрес вузлів у даній мережі - розробити функцію get_number_of_usable_hosts_from_raw_address(raw_address)
# класу мережі (A, B, C, D, E) - розробити функцію get_ip_class_from_raw_address(raw_address)
# чи адреса належить до простору приватних мереж (True/False) - розробити функцію check_private_ip_address_from_raw_address(raw_address)

    # >>> python ip_calc.py
    # 91.124.230.205/30
    # IP address: 91.124.230.205
    # Network Address: 91.124.230.204
    # Broadcast Address: 91.124.230.207
    # Binary Subnet Mask:	11111111.11111111.11111111.11111100
    # First usable host IP: 91.124.230.205
    # Penultimate usable host IP: 91.124.230.205
    # Number of usable Hosts: 2
    # IP class: A
    # IP type private: False

    # >>> python ip_calc.py
    # test
    # Error

    # >>> python ip_calc.py
    # 91.124.230.205
    # Missing prefix