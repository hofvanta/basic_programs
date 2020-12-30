def add_some(servers):
    """
    - voeg Helsinki toe aan het einde van de lijst
    - voeg ~Madrid~ toe tussen ~Tokyo~ en ~Paris~
    """

def get_five_letter_servers(servers):
    five_letter_names = ['Paris']  # fixture
    '''Doorloop de list servers. 
       indien de lengte van de servernaam lengte 5 heeft, 
       voeg dan toe aan five_letter_names'''


    return five_letter_names


def print_reverse(a_list):
    '''Maak een kopie van a_list mbv slicing.
       Gebruik list.pop() om van de gekopieerde lijst telkens
       het laatste item eruit te halen. print telkens het item. '''

def main():
    servers = ['Amsterdam', 'Tokyo', 'Paris', 'Brussel']
    add_some(servers)
    '''print het aantal servers'''

    filtered = get_five_letter_servers(servers)
    '''print het aantal vijf-letter-servers'''
    print_reverse(filtered)


if __name__ == "__main__":
    main()