from random import randint

def ask_min_max_numbers():
    ''' vraag minimale waarde
    vraag daarna in een oneindige loop een maximale waarde
    blijf in de loop als de maximale waarde kleiner is dan de minimale waarde
    break uit de loop als de maximale waarde groter is dan de minimale waarde
    en retourneer beide waarden
    '''
    min_waarde = int(input("Geef min waarde: "))
    while True:
        max_waarde = int(input("geef max waarde: "))
        if max_waarde > min_waarde:
            break
        print("Max nummer moet groter zijn dan", min_waarde)
    return min_waarde, max_waarde


def select_random_number(min, max):
    '''Start een oneindige loop waarin je een random getal genereert tussen min en max.
    Toon het nummer en vraag of dit getal geselcteerd moet worden
    Indien de gebruiker 'yes' ingeeft, retourneer je het getal.
    In alle andere gevallen zeg je dat je een een nieuw getal gaat maken en je blijft in de loop.
    '''
    while True:
        random_number = randint(min, max)
        print (random_number)
        userinput = input("Akkoord? : ")
        if 'y' in userinput.lower() or 'yes' in userinput.lower():
            return random_number
        print("Continue next number")

def main():
    min, max = ask_min_max_numbers()
    number = select_random_number(min, max)

    message = str(min) + "," + str(max)   # pretty print het resultaat. gebruik de + operator
    print(message)


if __name__ == "__main__":
    main()