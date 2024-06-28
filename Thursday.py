from datetime import date, datetime

class Thursday():
    def __init__(self, date: date) -> None:
        self.date = date
        self.meeting_list = []

    def display_thursday(self):
        self.meeting_list.sort(key=lambda meeting: meeting.time)
        formatted_date = datetime.strftime(self.date, "%m-%d-%Y")
        print(f"Date: {formatted_date}")
        for meeting in self.meeting_list:
            meeting_time_str = meeting.time.strftime("%I:%M %p")
            print(f"    {meeting_time_str} : {meeting.person.name}")
    
    @staticmethod
    def from_user_input():
        date_str = input("What is the date? (YYYY-MM-DD) ")

        date_obj = datetime.strptime(date_str, "%m-%d-%Y").date()

        return Thursday(date_obj)        
