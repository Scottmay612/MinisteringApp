from datetime import time

class Person():
    def __init__(self, name, phone_number, companion_name, is_finished = False, current_status = None, meeting_date = "TBD", meeting_time = "TBD"):
        self.name = name
        self.phone_number = phone_number
        self.companion = companion_name
        self.meeting_date = meeting_date
        self.meeting_time = meeting_time
        self.current_status = current_status
        self.is_finished = is_finished

    @classmethod
    def from_user_input(cls):
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        companion_name = input("Companion Name: ")
        return cls(name, phone_number, companion_name)
    

    def to_dict(self): # AI helped me learn how to do this.
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "companion": self.companion,
            "is_finished": self.is_finished,
            "current_status": self.current_status,
            "meeting_date": self.meeting_date,
            "meeting_time": self.meeting_time
                }


    def display_info(self):
        if isinstance(self.meeting_time, str):
            time_str = self.meeting_time
            date_str = self.meeting_date
        else:
            time_str = self.meeting_time.strftime("%I:%M %p")
            date_str = self.meeting_date.strftime("%Y-%m-%d")

        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Companion Name: {self.companion}")
        print(f"Meeting Date: {self.meeting_date}")
        print(f"Meeting Time: {time_str}")
        print(f"Finished: {self.is_finished}")
        print(f"Current Status: {self.current_status}")

    @staticmethod
    def from_dict(data):
        person = Person(name=data["name"], phone_number=data["phone_number"], companion_name=data["companion"],is_finished=data["is_finished"],current_status=data["current_status"],meeting_date=data["meeting_date"], meeting_time=data["meeting_time"])
        return person
        
        
    
