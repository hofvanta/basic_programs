import json

def ask_user_hostname():
    hostname = input("Hostname: ")
    return hostname.strip()

def ask_user_ip():
    ip = input("IP: ")
    return ip.strip()

def print_dns(dns):
    for key, value in dns.items():
        print(key, ', ', value)

def add_to_dns(dns, hostname, ip):
    if not hostname in dns:
        dns[hostname] = ip
    else:
        if ask_overwrite():
            dns[hostname] = ip

def user_wants_to_quit():
    do_quit = input("Quit? [Y/N] ").strip()

    if do_quit.lower() in ['y', 'yes', 'j', 'ja']:
        return True

def ask_overwrite():
    do_overwrite = input("Already existing, overwrite? [Y/N] ").strip()

    if do_overwrite.lower() in ['y', 'yes', 'j', 'ja']:
        return True

def user_interact(dns):
    while True:
        hostname = ask_user_hostname()
        ip = ask_user_ip()

        add_to_dns(dns, hostname, ip)
        print_dns(dns)

        if user_wants_to_quit():
            return


def export_json(dns):
    json_output = json.dumps(dns)
    print(json_output)

def main():
    dns = { 'rjekker.nl': '136.144.169.117' }
    user_interact(dns)
    export_json(dns)

if __name__ == "__main__":
    main()