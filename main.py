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


class Record:
    pass


class Notes:
    pass


class Bot:

    def __init__(self):

        self.Adderessbook = AddressBook()
        self.notes = []  # a func add_note should create an instance of Note
        # and add it to current list
        self.menu = "Hello guys! Lets get it started"  # should be changed

        print(self.menu)

        while True:

            command = input("I am waiting for your command: ")

            if command == "exit" or command == "15":
                print("Good bye!")
                break
            else:
                # carrying should fulfil the command
                pass

    def sort_files(self, file_name):
        # external sort func should be imported
        pass


if __name__ == "__main__":

    my_bot = Bot()
