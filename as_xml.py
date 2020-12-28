def indent(content, spaces):
    spaces = int(spaces/2)
    space_string = " " * spaces + content
    return space_string


def as_xml(content, tag_name):
    xml = '<' + tag_name + '>' + content + '</' + tag_name + '>'
    return xml


def main():
    name = "Paris"
    ip = "10.0.0.135"
    xml_name = as_xml(name, "name")
    xml_ip = as_xml(ip, "ip4")

    print(indent(xml_name, 0))
    print(indent(xml_ip, 4))


if __name__ == "__main__":
    main()