from Person import Person
from datetime import time

class Meeting():
    def __init__(self, person: Person, time: time,) -> None:
        self.time = time
        self.person = person

    