from Person import Person

class Directory():
    def __init__(self, people_list: list = []) -> None:
        self.people_list = people_list

    def add_person(self, person: Person):
        self.people_list.append(person)

    def sort_directory(self):
        self.people_list.sort(key=lambda person: person.name)

    def display_directory(self):
        sorted_list = self.sort_directory()
        for index, person  in enumerate(self.people_list):
            print(f"{index + 1}. {person.name}")

    def show_finished(self):
        finished_count = 0
        for person in self.people_list:
            if person.is_finished == True:
                finished_count += 1
                print(person.name)
        if finished_count == 0:
            print("There are no finished meetings yet.")
            print()

    def show_unfinished(self):
        unfinished_count = 0
        for person in self.people_list:

            if person.is_finished == False:
                unfinished_count += 1
                print(person.name)
        if unfinished_count == 0:
            print("All meetings are finished. ")
            print()
    
    def mark_meeting_finished(self):
        print("Which person finished?")
        self.show_unfinished()
        finished_person = input("Enter their name: ")
        finished_person_obj = self.find_person(finished_person)
        finished_person_obj.is_finished = True
    
    def find_person(self, name):
        for person in self.people_list:
            if person.name == name:
                return person
    
    def show_all_status(self):
        for person in self.people_list:
            print(f"{person.name}: ")
            print(person.current_status)
            print()