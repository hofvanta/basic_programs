def ask_number(minimum=0, max_tries=3):
    for trynum in range(max_tries):
        waarde = int(input("Waarde: "))
        if waarde >= minimum:
             return waarde
        print("Waarde niet kleiner dan ", minimum)
    return minimum


def generate_ip_addresses(start_octet, end_octet, base="192.168.178"):
    '''implementeer
       sanitize eventueel start en end
       print de adressen 192.168.178.start t/m 192.168.178.end
    '''
    for octet in range(start_octet, end_octet):
        address = base + '.' + str(octet)
        print(address)

def main():
    print("Hoeveel ip-adressen moeten er worden gemaakt?")
    ip_count = ask_number()

    print("Wat is het start-octet?")
    ip_start = ask_number(minimum=1, max_tries=2)
    ip_end = 255  # fixture, zelf bedenken!

    generate_ip_addresses(ip_start, ip_end)

if __name__ == "__main__":
    main()