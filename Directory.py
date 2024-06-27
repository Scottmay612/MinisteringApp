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
            print(f"{index + 1}. {person.name}")

    def mark_meeting_finished(self, choice):
        choice = choice - 1
        finished_person = self.people_list[choice]
        finished_person.is_finished = True

    def show_finished(self):
        for person in self.people_list:
            if person.is_finished == True:
                print(person.name)
    
    def show_unfinished(self):
        for person in self.people_list:
            if person.is_finished == False:
                print(person.name)
    
    def find_person(self, name):
        for person in self.people_list:
            if person.name == name:
                return person
    
    def show_all_status(self):
        for person in self.people_list:
            print(f"{person.name}: ")
            print(person.current_status)
            print()