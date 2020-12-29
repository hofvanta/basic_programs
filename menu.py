import sys


def load_confuration():
    print("Loading configuration")

def save_configuration():
    print("Saving confuration")

def quit():
    print("Quiting")

def what_to_do():
   action = input("Give the action: ")
   if action.lower() == "load":
      load_confuration()
   elif action.lower() == "save":
      save_configuration()
   elif action.lower() == "quit":
       quit()
   else:
       print("Unknown action")

def main():
    what_to_do()

main()