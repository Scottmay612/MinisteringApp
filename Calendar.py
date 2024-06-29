from datetime import date
from Thursday import Thursday
from Meeting import Meeting

class Calendar():
    def __init__(self) -> None:
        # Initialize attribute.
        self.thursdays_list = []
    
    # Add a thursday object the calendar.
    def add_thursday(self, thursday: Thursday):
        self.thursdays_list.append(thursday)

    # Display the calendar with all of the Thursdays scheduled.
    def display_calendar(self):

        # Sort the thursdays by date.
        self.thursdays_list.sort(key=lambda thursday: thursday.date)

        # Display each thursday as long as their is a meeting in it.
        for thursday in self.thursdays_list:
            if thursday.date >= date.today() and len(thursday.meeting_list) > 0:
                thursday.display_thursday()
                print()
    
    # Add a meeting to a specific thursday.
    def add_meeting_to_thursday(self, meeting: Meeting):
        thursday_exists = False

        # Check to see if there is already a thursday setup for that date and add the meeting.
        for thursday in self.thursdays_list:
            if thursday.date == meeting.date:
                thursday.meeting_list.append(meeting)
                thursday_exists = True
        
        # Create a new thursday and add a meeting to it.
        if thursday_exists == False:
            new_thursday = Thursday(meeting.date)
            new_thursday.meeting_list.append(meeting)
            self.thursdays_list.append(new_thursday)

    # Delete a persons meeting and reset their meeting time and date to "TBD".
    def delete_meeting(self, person_name):
        for thursday in self.thursdays_list:
            for index, meeting in enumerate(thursday.meeting_list):
                if meeting.person.name == person_name:
                    thursday.meeting_list.pop(index)
                    meeting.person.meeting_date = "TBD"
                    meeting.person.meeting_time = "TBD"


    
        