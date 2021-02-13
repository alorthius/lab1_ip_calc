"""
GitHub link: https://github.com/alorthius/lab2_ip_calc
"""


def check_users_input(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return 'Error'
    elif '/' not in raw_address:
        return 'Missing prefix'    


def get_ip_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    return raw_address[: raw_address.find('/')]


def get_binary_ip(ip_address: str) -> str:
    """
    """
    if not isinstance(ip_address, str):
        return None

    ip_list = ip_address.split('.')
    binary_ip = []

    for num in ip_list:
        binary_num = str(bin(int(num)))[2:]

        if len(binary_num) != 8:
            binary_num = '0' * (8 - len(binary_num)) + binary_num
        binary_ip.append(binary_num)

    return '.'.join(binary_ip)


def get_mask_number(raw_address: str) -> int:
    """
    """
    if not isinstance(raw_address, str):
        return None

    return int(raw_address[raw_address.find('/') + 1:])


def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    empty_mask = '00000000.00000000.00000000.00000000'
    mask_num = get_mask_number(raw_address)
    binary_mask = empty_mask.replace('0', '1', mask_num)
    return binary_mask


def convert_binary_to_numbers(binary_row: str) -> str:
    """
    """
    if not isinstance(binary_row, str):
        return None

    return '.'.join([str(int(num, 2)) for num in binary_row.split('.')])


def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    binary_ip = get_binary_ip(get_ip_from_raw_address(raw_address))
    binary_mask = get_binary_mask_from_raw_address(raw_address)

    network_address = []
    for ip_index, ip_num in enumerate(binary_ip):
        for mask_index, mask_num in enumerate(binary_mask):
            if ip_index == mask_index:
                try:
                    network_address.append(str(int(ip_num) & int(mask_num)))
                except ValueError:
                    network_address.append('.')

    return convert_binary_to_numbers(''.join(network_address))


def get_inverted_mask(mask_number: int) -> str:
    """
    """
    if not isinstance(mask_number, int):
        return None

    empty_mask = '11111111.11111111.11111111.11111111'
    return empty_mask.replace('1', '0', mask_number)


def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    binary_ip = get_binary_ip(get_ip_from_raw_address(raw_address))
    inverted_mask = get_inverted_mask(get_mask_number(raw_address))

    broadcast_address = []
    for index in range(0, 35):
        try:
            broadcast_address.append(
                str(int(binary_ip[index]) | int(inverted_mask[index])))
        except ValueError:
            broadcast_address.append('.')

    return convert_binary_to_numbers(''.join(broadcast_address))


def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    network_address = get_network_address_from_raw_address(raw_address)
    return network_address[:-3] + str(int(network_address[-3:]) + 1)


def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    broadcast_address = get_broadcast_address_from_raw_address(raw_address)
    return broadcast_address[:-3] + str(int(broadcast_address[-3:]) - 2)


def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    """
    """
    if not isinstance(raw_address, str):
        return None

    mask_number = get_mask_number(raw_address)
    return 2 ** (32 - mask_number) - 2


def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    """
    if not isinstance(raw_address, str):
        return None

    ip_address = get_ip_from_raw_address(raw_address)
    first_octet = int(ip_address[:ip_address.find('.')])

    if first_octet <= 127:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'


def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    """
    if not isinstance(raw_address, str):
        return None

    ip_address = get_ip_from_raw_address(raw_address)
    first_octet = int(ip_address[:ip_address.find('.')])

    if first_octet == 10:
        return True
    elif first_octet == 172:
        if 16 <= int(ip_address[4: 6]) <= 31:
            return True
    elif first_octet == 192:
        if int(ip_address[4: 7]) == 168:
            return True

    return False
