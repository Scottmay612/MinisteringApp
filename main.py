from Person import Person
from JSON_handler import JSON_handler
from Meeting import Meeting
from Directory import Directory
from Calendar import Calendar
import time
import os

# Create a list to store Person objects
person_list = []

continue_response = ""

# Create a list of menu options.
main_menu_options = [
    "Display Calendar",
    "Manage People",
    "Manage Meetings",
    "Quit"
    ]

people_manage_options = [
    "Add New Person",
    "Show Directory",
    "Update Status",
    "Show Each Status",
    "Show Unfinished",
    "Show Finished",
    "Mark As Finished",
    "Return to Main Menu"
]

meeting_manage_options = [
    "Add New Meeting",
    "Delete Meeting",
    "Return to Main Menu"
]

# Create a sample person and add to the list

def main():
    directory = Directory()
    calendar = Calendar()

    update_all_info(directory, calendar)

    menu_choice = None
    people_manage_choice = None
    meeting_manage_choice = None

    main_quit_option = len(main_menu_options)
    people_quit_option = len(people_manage_options)
    meeting_quit_option = len(meeting_manage_options)

    while menu_choice != main_quit_option:
        # Clear the terminal.
        os.system("cls")

        # Display menu options.
        print("What would you like to do?")
        display_menu(main_menu_options)

        menu_choice = input("Pick a number: ")
        os.system("cls")

        match(menu_choice):
            case "1":
                print("CALENDAR")
                print()
                calendar.display_calendar()
                input("Press enter to continue: ")

            case "2":
                os.system("cls")
                while people_manage_choice != people_quit_option:
                    os.system("cls")
                    print("PEOPLE MANAGEMENT")
                    display_menu(people_manage_options)
                    people_manage_choice = input("Select a number: ")
                    os.system("cls")
                        
                    match(people_manage_choice):
                        case "1":
                            person = Person.from_user_input()
                            directory.add_person(person)
                        case "2":
                            print("DIRECTORY")
                            directory.display_directory()
                            input("Press enter to continue: ")
                        case "3":
                            people_manage_person = input("What is the name? ")
                            new_status = input("What is the new status? ")
                            people_manage_person = directory.find_person(people_manage_person)
                            people_manage_person.current_status = new_status
                        case "4":
                            directory.show_all_status()
                            input("Press enter to continue: ")
                        case "5":
                            directory.show_unfinished()
                            input("Press enter to continue: ")
                        case "6": 
                            directory.show_finished()
                            input("Press enter to continue: ")
                        case "7":
                            directory.mark_meeting_finished()
                            print("Meeting Recorded")
                            time.sleep(2)
                        case "8":
                            break
                                       
            case "3": 
                while meeting_manage_choice != meeting_quit_option:
                    os.system("cls")
                        
                    print("MEETING MANAGEMENT")
                    print("What would you like to do?")
                    display_menu(meeting_manage_options)
                    meeting_manage_choice = input("Select a number: ")
                    os.system("cls")
                    match(meeting_manage_choice):
                        case "1":
                            meeting = Meeting.from_user_input(directory)
                            calendar.add_meeting_to_thursday(meeting)
                            print("Meeting Added")
                            time.sleep(2)
                        case "2":
                            person_meeting_delete = input("What is the name? ")
                            calendar.delete_meeting(person_meeting_delete)
                            print("Meeting Deleted")
                            time.sleep(2)
                        case "3":
                            break               
                
            case "4":
                people_dict = [person.to_dict() for person in directory.people_list]
                JSON_handler.write_to_file(people_dict)       
                break
            case _:
                print("Invalid option")
                break

def display_menu(options):
    for index, option in enumerate(options):
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
