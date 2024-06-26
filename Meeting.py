from Person import Person
from datetime import time, date, datetime

class Meeting():
    def __init__(self, person: Person, time: time, date: date) -> None:
        self.time = time
        self.date = date
        self.person = person
    
    def display_meeting(self):
        print(f"Name: {self.person.name}")
        print(f"Time: {self.time}")
        
    @staticmethod
    def from_user_input(cls, person):
        person = person
        time_str = input("What is the time? (HH:MM)") 
        date_str = input("What is the date? (MM-DD-YYYY)")

        time_obj = datetime.strptime(time_str, "%H:%M").time()
        date_obj = datetime.strptime(date_str, "%M:%D:%Y").date()

        return Meeting(person, time_obj, date_obj)

    