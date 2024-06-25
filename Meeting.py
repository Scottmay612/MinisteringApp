from Person import Person
from datetime import time
from datetime import date

class Meeting():
    def __init__(self, person: Person, time: time, date: date) -> None:
        self.time = time
        self.date = date
        self.person = person

    