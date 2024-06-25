class Person():
    def __init__(self, name, phone_number, companion_name, is_finished = False, current_status = "", meeting_date = "TBD", meeting_time = "TBD"):
        self.name = name
        self.phone_number = phone_number
        self.companion = companion_name
        self.meeting_date = meeting_date
        self.current_status = current_status
        self.meeting_time = meeting_time
        self.is_finished = is_finished

    @classmethod
    def from_user_input(cls):
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        companion_name = input("Companion Name: ")
        return cls(name, phone_number, companion_name)



    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Companion Name: {self.companion}")
        print(f"Meeting Date: {self.meeting_date}")
        print(f"Meeting Time: {self.meeting_time}")
        print(f"Finished: {self.is_finished}")
        print(f"Current Status: {self.current_status}")
        
    
