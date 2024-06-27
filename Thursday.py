from datetime import date

class Thursday():
    def __init__(self, date: date) -> None:
        self.date = date
        self.meeting_list = []

    def display_thursday(self):
        self.meeting_list.sort(key=lambda meeting: meeting.time)
        print(f"Date: {self.date}")
        for meeting in self.meeting_list:
            meeting_time_str = meeting.time.strftime("%I:%M %p")
            print(f"    {meeting_time_str} : {meeting.person.name}")
    
    @staticmethod
    def from_user_input():
        date_str = input("What is the date? (YYYY-MM-DD) ")

        date_obj = date.fromisoformat(date_str)

        return Thursday(date_obj)        
