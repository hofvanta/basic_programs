def ask_amount():
    '''Asks the user for an amount.

    Prints an error if the amount is smaller that 0 and returns 0.
    Else it will return the amount of the user.'''
    waarde = float(input("Geef de waarde: "))
    if waarde < 0:
        print("Negatief getal")
        return 0
    else:
        return waarde


def main():
    amount = ask_amount()
    message = "The user wants " + str(amount)
    print(message)


main()