from Meeting import Meeting
class Thursday():
    def __init__(self, meeting_1: Meeting, meeting_2: Meeting, meeting_3: Meeting, meeting_4: Meeting) -> None:
        self.meeting_1 = meeting_1
        self.meeting_2 = meeting_2
        self.meeting_3 = meeting_3
        self.meeting_4 = meeting_4

    def display_thursday(self):
        print(f"7:45: {self.meeting_1.person}")
        print(f"")