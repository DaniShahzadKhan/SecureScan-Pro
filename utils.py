import ipaddress

def validate_ip(ip):
    """
    Returns True if the IP address is valid, otherwise False.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
