from Person import Person

class Directory():
    def __init__(self, people_list: list = []) -> None:
        self.people_list = people_list

    def add_person(self, person: Person):
        self.people_list.append(person)

    def sort_directory(self):
        self.people_list.sort(key=lambda person: person.name)

    def display_directory(self):
        for index, person  in enumerate(self.people_list):
            print(f"{index + 1}. {person.display_info()}")
    