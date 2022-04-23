from collections import UserDict


class AddressBook(UserDict):

    def __init__(self):
        pass


class Field:

    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return f"{self.__value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass


class Note(Field):
    pass


class NotesBook(UserDict):

    def __init__(self):
        self.data = []

    def add_note(self, note: Note):
        added_note = {'id': '', 'tag': '', 'note': note}
        self.data.append(added_note)

    def print_menu(self):
        while True:
            command = input('''Do you want create notes or check?
                            Create: enter 1 or create
                            Check: enter 2 or check
                            If you need exit, enter exit or 0\n''').lower()
            if command == '1' or command == 'create':
                note = Note(input('Enter your notes: '))
                self.add_note(note)
            elif command == '2' or command == 'check':
                print(self.data)
            elif command == '0' or command == 'exit':
                break


class Record:
    pass


class Bot:

    def __init__(self):

        self.address_book = AddressBook()
        self.notes_book = NotesBook()
        #self.notes = []  # a func add_note should create an instance of Note
        # and add it to current list
        self.menu = "Hello guys! Lets get it started"  # should be changed

        print(self.menu)

        while True:

            command = input("I am waiting for your command: ")

            if command == "exit" or command == "15":
                print("Good bye!")
                break
            elif command == "note" or command == "14":  #number may be change
                self.notes_book.print_menu()

            else:
                # carrying should fulfil the command
                pass

    def sort_files(self, file_name):
        # external sort func should be imported
        pass


if __name__ == "__main__":
    my_bot = Bot()
