from Person import Person

class Directory():
    def __init__(self, people_list: list = []) -> None:
        self.people_list = people_list

    def add_person_to_directory(self):
        self.people_list.append(Person)

    def sort_directory(self):
        self.people_list.sort(key=lambda person: person.name)

    def display_directory(self):
        for person, index in enumerate(self.people_list):
            print(f"{index + 1}. {person.name}")
    