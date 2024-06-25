from Meeting import Meeting

class Thursday():
    def __init__(self, meeting_1: Meeting, meeting_2: Meeting, meeting_3: Meeting, meeting_4: Meeting) -> None:
        self.meeting_list = [meeting_1, meeting_2, meeting_3, meeting_4]
        self.meeting_list.sort(key=lambda meeting: meeting.time)

    def display_thursday(self):
        for meeting in self.meeting_list:
            print(f"{meeting.time}: {meeting.person}")