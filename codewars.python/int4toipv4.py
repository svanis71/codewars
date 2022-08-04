def int32_to_ip(n: int) -> str:
    return '.'.join((str(n >> (x * 8) & 0xff)) for x in range(3, -1, -1))
