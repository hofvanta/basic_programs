def build_url(hostname, path, type, port=443, ext=".html"):
    url = "https://" + hostname + ":" + str(port) + "/" + path + type + ext
    return url


def main():
    url = build_url("service.org", "api/v2/", "servers", port=7700, ext=".json")
    print(url)
    url = build_url("service.org", "api/v2/", "routers")
    print(url)

if __name__ == "__main__":
    main()