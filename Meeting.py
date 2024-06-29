from Person import Person
from datetime import time, date, datetime
from Directory import Directory

class Meeting():
    def __init__(self, person: Person, time: time, date: date) -> None:
        # Initializing attributes.
        self.time = time
        self.date = date
        self.person = person
    
    # Displays the meeting to the user.
    def display_meeting(self):
        print(f"Name: {self.person.name}")
        print(f"Time: {self.time}")

    # A method that gets the users input to create an instance of the class.
    @staticmethod
    def from_user_input(directory: Directory):
        desired_person = None

        # Get the persons name.
        person_name = input("Who is the meeting for? ")

        # Find the person and return their persob object.
        for person in directory.people_list:
            if person.name == person_name:
                desired_person = person
        
        # Get the users date and time for the meeting.
        time_str = input("What is the time? (HH:MM AM/PM) ") 
        date_str = input("What is the date? (MM-DD-YYYY) ")

        # Turn the dates and times into objects respectively.
        time_obj = datetime.strptime(time_str, "%I:%M %p").time()
        date_obj = datetime.strptime(date_str, "%m-%d-%Y").date()

        # Update the persons instance information.
        desired_person.meeting_time = time_obj
        desired_person.meeting_date = date_obj

        # Return the meeting instance.
        return Meeting(desired_person, time_obj, date_obj)
    


    