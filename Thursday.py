from datetime import date, datetime

class Thursday():
    def __init__(self, date: date) -> None:
        # Initialize the attributes.
        self.date = date
        self.meeting_list = []

    def display_thursday(self):
        # Sort the meetings by their time.
        self.meeting_list.sort(key=lambda meeting: meeting.time) # Chat GPT showed me how to do this.

        # Format that date into a nice string.
        formatted_date = datetime.strftime(self.date, "%m-%d-%Y")

        # Display the meetings for that day.
        print(f"Date: {formatted_date}")
        for meeting in self.meeting_list:
            meeting_time_str = meeting.time.strftime("%I:%M %p")
            print(f"    {meeting_time_str} : {meeting.person.name}")
    
