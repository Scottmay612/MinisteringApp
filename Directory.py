from Person import Person

class Directory():
    def __init__(self, people_list: list = []) -> None:
        # Declare attribute.
        self.people_list = people_list

    # Adds a person object to the directory.
    def add_person(self, person: Person):
        self.people_list.append(person)
        self.people_list.sort(key=lambda person: person.name) #ChatGPT showed me how to do this.

    # Displays a numbered list of the directory.
    def display_directory(self):
        for index, person  in enumerate(self.people_list):
            print(f"{index + 1}. {person.name}")

    # Shows all of the people who have finished their meeting.
    def show_finished(self):
        finished_count = 0
        for person in self.people_list:
            if person.is_finished == True:
                finished_count += 1
                print(person.name)

        # If there are no finished meetings, tell the user.
        if finished_count == 0:
            print("There are no finished meetings yet.")
            print()

    # Shows all of the people who haven't finished their meeting yet.
    def show_unfinished(self):
        unfinished_count = 0
        for person in self.people_list:

            if person.is_finished == False:
                unfinished_count += 1
                print(person.name)

        # If there are no unfinished meetings, tell the user.
        if unfinished_count == 0:
            print("All meetings are finished. ")
            print()
    
    # Marks a specific persons meeting as finished.
    def mark_meeting_finished(self):
        print("Which person finished?")
        self.show_unfinished()
        finished_person = input("Enter their name: ")
        finished_person_obj = self.find_person(finished_person)
        finished_person_obj.is_finished = True
    
    # Returns the persons person object when the user inputs their name.
    def find_person(self, name):
        for person in self.people_list:
            if person.name == name:
                return person
    
    # Show just the status of each person.
    def show_all_status(self):
        for person in self.people_list:
            print(f"{person.name}: ")
            print(person.current_status)
            print()
    
    # Shows each companion ships names.
    def show_companionships(self):
        for person in self.people_list:
            print(f"{person.name} | {person.companion}")
            print()