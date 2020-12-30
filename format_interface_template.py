def ask_interface_properties():
    int_name = input("interface: ")
    int_description = input("description: ")
    int_type = input("type: ")
    int_enabled = input("enabled [true/false]:")
    int_ip_address = input("ip addres: ")
    int_netmask = input("netmask: ")
    properties = {"name":int_name,
                  "description":int_description,
                  "type":int_type,
                  "enabled":int_enabled,
                  "ip_address":int_ip_address,
                  "netmask":int_netmask}
    return properties


def get_interface_config(interface_data):
    '''Laad de template van file en vul met interface_data'''
    with open("templates/netconf_interface_template.xml", "r") as f:
        xml = f.read()
    xmlconfig = xml.format(**interface_data)
    return xmlconfig


def main():
    interface_data = ask_interface_properties()
    interface_config = get_interface_config(interface_data)
    print(interface_config)


if __name__ == "__main__":
    main()