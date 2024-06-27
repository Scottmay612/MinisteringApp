from Person import Person
from JSON_handler import JSON_handler
from Meeting import Meeting
from Directory import Directory
from Calendar import Calendar
from datetime import date, time, datetime
import os

# Create a list to store Person objects
person_list = []

continue_response = ""

# Create a list of menu options.
menu_options = ["See Directory", 
                "Add New Person", 
                "Add New Meeting", 
                "Add New Thursday", 
                "Display Calendar",
                "Mark As Finished",
                "Quit"]

# Create a sample person and add to the list

def main():
    directory = Directory()
    calendar = Calendar()

    try:
        update_all_info(directory, calendar)
    except:
        print("The file is empty.")
        input()

    menu_choice = None
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
                print("DIRECTORY")
                print()
                directory.display_directory()
                input("Press enter to continue: ")
            case "2":
                person = Person.from_user_input()
                directory.add_person(person)
            case "3": 
                meeting = Meeting.from_user_input(directory)
                calendar.add_meeting_to_thursday(meeting)
            case "4":
                print()
            case "5":
                calendar.display_calendar()
                input()
            case "6":
                input()
            case "7":
                people_dict = [person.to_dict() for person in directory.people_list]
                JSON_handler.write_to_file(people_dict)
                    
                break

            case _:
                print("Invalid option")
                break

def display_menu():
    for index, option in enumerate(menu_options):
        print(f"{index + 1}. {option}")

def update_all_info(directory: Directory, calendar: Calendar):
    json_data = JSON_handler.read_file()
    person = [Person.from_dict(person_data) for person_data in json_data]
    for p in person:
        directory.add_person(p)
        if p.meeting_date != "TBD":
            p.meeting_time = JSON_handler.deserialize_times(p.meeting_time)
            p.meeting_date = JSON_handler.deserialize_dates(p.meeting_date)
            calendar.add_meeting_to_thursday(
                Meeting(
                    p, 
                    p.meeting_time, 
                    p.meeting_date))

if __name__ == "__main__":
    main()
