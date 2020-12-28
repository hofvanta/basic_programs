# projects/basic_programs/basic_program.py

def main():
    # here starts your program
    server_name = input ("What is server name: ")
    ip_address = input("What is the IP Address: ")
    net_mask = input("What is the netmask: ")
    print("-------------")
    print(server_name + "," + ip_address + "," + net_mask)
    print("=============")
    print("Servername: ", server_name.strip())
    print("IP: ", ip_address.strip())
    print("Netmask: ", net_mask.strip())

# kick off the function main
main()