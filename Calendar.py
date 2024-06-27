from datetime import date
from Thursday import Thursday
from Meeting import Meeting

class Calendar():
    def __init__(self) -> None:
        self.thursdays_list = []
    
    def add_thursday(self, thursday: Thursday):
        self.thursdays_list.append(thursday)

    def display_calendar(self):
        for thursday in self.thursdays_list:
            if thursday.date >= date.today():
                thursday.display_thursday()
    
    def add_meeting_to_thursday(self, meeting: Meeting):
        thursday_exists = False

        for thursday in self.thursdays_list:
            if thursday.date == meeting.date:
                thursday.meeting_list.append(meeting)
                thursday_exists = True

        if thursday_exists == False:
            new_thursday = Thursday(meeting.date)
            new_thursday.meeting_list.append(meeting)
            self.thursdays_list.append(new_thursday)

    def delete_meeting(self, person_name):
        for thursday in self.thursdays_list:
            for index, meeting in enumerate(thursday.meeting_list):
                if meeting.person.name == person_name:
                    thursday.meeting_list.pop(index)
                    meeting.person.meeting_date = "TBD"
                    meeting.person.meeting_time = "TBD"


    
        