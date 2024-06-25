from Person import Person
from Directory import Directory
import os

# Create a list to store Person objects
person_list = []

continue_response = ""

# Create a list of menu options.
menu_options = ["See Directory", 
                "See Finished People", 
                "See Remaining People", 
                "Add To List", 
                "Add Meeting Time",
                "Mark As Finished",
                "Quit"]

# Create a sample person and add to the list
person = Person("Scott", "435-849-5380", "Natalya")
directory = Directory()
Directory.append(person)

def main():
    menu_choice = ""
    quit_option = len(menu_options)

    while menu_choice != quit_option:
        # Clear the terminal.
        os.system("cls")

        # Display menu options.
        print("What would you like to do?")
        display_menu()

        menu_choice = input("Pick a number: ")
        os.system("cls")

        match(menu_choice):
            case "1":
                print("ALL PEOPLE")
                print()
                directory.display_directory()
                input("Press enter to continue: ")
            case "2":
                for person in person_list:
                    if person.is_finished == True:
                        person.display_info()
                        print()
                input("Press enter to continue: ")
            case "3": 
                for person in person_list:
                    if person.is_finished == False:
                        person.display_info()
                        print()
                input("Press enter to continue: ")
            case "4":
                add_person()
            case "5":
                display_people_list()
            case "6":
                print()
            case "7":
                for person in Directory:
                    person.to_dict()
                    
                break

            case _:
                print("Invalid option")
                break

def display_menu():
    for index, option in enumerate(menu_options):
        print(f"{index + 1}. {option}")

def display_people_list():
    for person in person_list:
        person.display_info()
        print()

def add_person():
    while continue_response == "":
        new_person = Person.from_user_input()
        person_list.append(new_person)

        continue_response = input("Press enter to continue: ")

if __name__ == "__main__":
    main()
