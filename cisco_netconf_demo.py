import xmltodict
from ncclient import manager

device = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": 10000,
    "username": "developer",
    "password": "C1sco12345"
}

def get_capabilities():
    with manager.connect(host=device['host'],
                         port=device['port'],
                         username=device['username'],
                         password=device['password'],
                         hostkey_verify=False) as m:
        for capability in m.server_capabilities:
            print(capability)


def get_config():
    with manager.connect(host=device['host'],
                         port=device['port'],
                         username=device['username'],
                         password=device['password'],
                         hostkey_verify=False) as m:
        return m.get_config("running")


response = get_config()

data = xmltodict.parse(response.xml)["rpc-reply"]["data"]
# for interface in data["interfaces"]:
#     for inter in interface["interface"]:
#         print(inter["name"])
#         print(inter["config"])



gigabit_interface = data["interfaces"][1]["interface"]
# for interface in gigabit_interface:
#     print(interface["name"])
#     if interface["ipv4"].get("address"):
#         print(interface["ipv4"]["address"]["ip"])
#         print(interface["ipv4"]["address"]["netmask"])

for interface in gigabit_interface:
    print(interface["name"])
    try:
        print(interface["ipv4"]["address"]["ip"])
        print(interface["ipv4"]["address"]["netmask"])
    except:
        print("no ip address")
        print("no ip netmask")

for interface in gigabit_interface:
    print("\ninterface", interface["name"])
    try:
        print("  ip address", interface["ipv4"]["address"]["ip"], interface["ipv4"]["address"]["netmask"])
    except:
        print("  no ip address")