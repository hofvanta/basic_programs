def print_device_properties():
    name = "GigabitEthernet2"
    ip = "192.168.1.55"
    netmask = "255.255.255.0"

    template = '''
    Name:       {name}
    IP Address: {ip}
    Netmask:    {netmask}
    '''
    print(template.format(name=name, ip=ip, netmask=netmask))



def main():
    print_device_properties()


main()