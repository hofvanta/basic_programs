import os, os.path

def ask_servernames(filepath):
    outfile = open(filepath, 'w')
    while True:
        servername = input("Servername: ").strip()
        if servername == "":
            break
        #print(servername, file=outfile)
        outfile.write(servername + '\n')
    outfile.close()
    return

def print_names_from_file(filename):
    infile = open(filename)

    for line in infile:
        print(line.strip())


def main():
    outfile = os.path.join(os.getcwd(), 'data', 'servernames.txt')
    ask_servernames(outfile)
    print_names_from_file(outfile)


if __name__ == "__main__":
    main()