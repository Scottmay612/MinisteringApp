from Person import Person
from datetime import time, date, datetime
from Directory import Directory

class Meeting():
    def __init__(self, person: Person, time: time, date: date) -> None:
        self.time = time
        self.date = date
        self.person = person
    
    def display_meeting(self):
        print(f"Name: {self.person.name}")
        print(f"Time: {self.time}")
        
    # @staticmethod
    def fix_date_input(date_str):
        date_parts = date_str.split("/")
        new_string = f"{date_parts[2]}-{date_parts[0]}-{date_parts[1]}"
        return new_string

    # @staticmethod
    def from_user_input(directory: Directory):
        desired_person = None
        person_name = input("Who is the meeting for? ")
        for person in directory.people_list:
            if person.name == person_name:
                desired_person = person
        time_str = input("What is the time? (HH:MM AM/PM) ") 
        date_str = input("What is the date? (MM/DD/YYYY) ")
        # date_str_formatted = fix_date_input(date_str)

        time_obj = datetime.strptime(time_str, "%I:%M %p").time()
        date_obj = datetime.strptime(date_str, "%m-%d-%Y").date()
        desired_person.meeting_time = time_obj
        desired_person.meeting_date = date_obj

        return Meeting(desired_person, time_obj, date_obj)
    


    