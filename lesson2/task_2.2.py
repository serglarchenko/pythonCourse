import re
import socket

try_yourself = """
assert check_ip('') is False
assert check_ip('192.168.0.1') is True
assert check_ip('0.0.0.1') is True
assert check_ip('10.100.500.32') is False
assert check_ip(700) is False
assert check_ip('127.0.1') is True ???? IP-адреса обычно выражаются в десятичном формате с точками с четырьмя числами, разделенными точками
"""
regexp_string = "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$"


def check_ip_regexp(regexp_pattern, ip_address):
    return bool(re.match(regexp_pattern, ip_address))


def check_ip_socket(string_ip):
    return bool(socket.inet_aton(string_ip))


print(check_ip_regexp(regexp_string, "192.168.123.132"))
print(check_ip_socket("127.0.0.1"))
