from Person import Person
from JSON_handler import JSON_handler
from Meeting import Meeting
from Directory import Directory
from Calendar import Calendar
import time
import os

# Create a list to store Person objects.
person_list = []

# Create a list of main menu options.
main_menu_options = [
    "Display Calendar",
    "Manage People",
    "Manage Meetings",
    "Quit"
]

# Create a list of options for managing people.
people_manage_options = [
    "Add New Person",
    "Show Directory",
    "Show Companionships",
    "Update Status",
    "Show Each Status",
    "Show Unfinished",
    "Show Finished",
    "Mark As Finished",
    "Return to Main Menu"
]

# Create a list of options for managing meetings.
meeting_manage_options = [
    "Add New Meeting",
    "Delete Meeting",
    "Return to Main Menu"
]

# Main function to drive the program.
def main():
    directory = Directory()  # Create an instance of Directory.
    calendar = Calendar()    # Create an instance of Calendar.

    # Update directory and calendar with existing data from JSON.
    try:
        update_all_info(directory, calendar)
    except:
        print("The file is empty.")

    menu_choice = None
    people_manage_choice = None
    meeting_manage_choice = None

    # Get the quit options for the menus.
    main_quit_option = len(main_menu_options)
    people_quit_option = len(people_manage_options)
    meeting_quit_option = len(meeting_manage_options)

    while menu_choice != main_quit_option:
        # Clear the terminal.
        os.system("cls")

        # Display the main menu options.
        print("MAIN MENU")
        display_menu(main_menu_options)

        # Get user choice for main menu.
        menu_choice = input("Pick a number: ")
        os.system("cls")

        match(menu_choice):
            case "1":
                # Display the calendar.
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
                            # Add a new person to the directory.
                            person = Person.from_user_input()
                            directory.add_person(person)

                        case "2":
                            # Display the directory.
                            print("DIRECTORY")
                            directory.display_directory()
                            input("Press enter to continue: ")

                        case "3":
                            # Show companionships.
                            print("COMPANIONSHIPS")
                            directory.show_companionships()
                            input("Press enter to continue: ")

                        case "4":
                            # Update the status of a person.
                            people_manage_person = input("What is the name? ")
                            new_status = input("What is the new status? ")
                            people_manage_person = directory.find_person(people_manage_person)
                            people_manage_person.current_status = new_status
                            
                        case "5":
                            # Show all statuses.
                            print("ALL STATUSES")
                            directory.show_all_status()
                            input("Press enter to continue: ")

                        case "6":
                            # Show unfinished tasks.
                            print("UNFINISHED")
                            directory.show_unfinished()
                            input("Press enter to continue: ")

                        case "7": 
                            # Show finished tasks.
                            print("FINISHED")
                            directory.show_finished()
                            input("Press enter to continue: ")

                        case "8":
                            # Mark a meeting as finished.
                            directory.mark_meeting_finished()
                            print("Meeting Recorded")
                            time.sleep(2)

                        case "9":
                            # Return to main menu.
                            break
                                       
            case "3": 
                while meeting_manage_choice != meeting_quit_option:
                    os.system("cls")
                        
                    print("MEETING MANAGEMENT")
                    display_menu(meeting_manage_options)
                    meeting_manage_choice = input("Select a number: ")
                    os.system("cls")

                    match(meeting_manage_choice):
                        case "1":
                            # Add a new meeting.
                            meeting = Meeting.from_user_input(directory)
                            calendar.add_meeting_to_thursday(meeting)
                            print("Meeting Added")

                            # Allow the user to read the confirmation message.
                            time.sleep(1)

                        case "2":
                            # Delete a meeting.
                            person_meeting_delete = input("What is the name? ")
                            calendar.delete_meeting(person_meeting_delete)
                            print("Meeting Deleted")

                            # Allow the user to read the confirmation message.
                            time.sleep(1)

                        case "3":
                            # Return to main menu.
                            break               
                
            case "4":
                # Save the current state and quit the program.
                people_dict = [person.to_dict() for person in directory.people_list]
                JSON_handler.write_to_file(people_dict)       
                break

            case _:
                # Handle invalid inputs.
                print("Invalid option")
                break

# Function to display a menu with given options.
def display_menu(options):
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

# Function to update directory and calendar with data from JSON.
def update_all_info(directory: Directory, calendar: Calendar):
    json_data = JSON_handler.read_file()

    # Make a list of people objects from the json data.
    person_data_list = [Person.from_dict(person_data) for person_data in json_data] # Chat GPT showed me how to do this.

    # Iterate through the people and add them to the directory. 
    for person in person_data_list:
        directory.add_person(person)

        # Recreate any date and time objects.
        if person.meeting_date != "TBD":
            person.meeting_time = JSON_handler.deserialize_times(person.meeting_time)
            person.meeting_date = JSON_handler.deserialize_dates(person.meeting_date)

            # Recreate the person's meeting if they have one and add it to the calendar.
            calendar.add_meeting_to_thursday(
                Meeting(
                    person, 
                    person.meeting_time, 
                    person.meeting_date))

# Run the main function if the script is executed directly.
if __name__ == "__main__":
    main()
