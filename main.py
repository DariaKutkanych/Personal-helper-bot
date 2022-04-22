# TODO Cохранять контакты с именами, адресами, номерами телефонов, email и днями рождения в книгу контактов;
   
from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def __init__(self):
        pass

    def add_record(self,set):
        self.data.__setitem__(set.name, (set.adresses, set.phones, set.emails, set.birthday))


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
    def __init__(self, n):
        self.name = n


class Phone(Field):
    def __init__(self, phone = None):
        self.phone = phone

class Birthday(Field):
     def __init__(self, birthday_y = None, birthday_m = None, birthday_d = None,):
        self.birthday = datetime (birthday_y, birthday_m, birthday_d)


class Adress(Field):
    def __init__(self, adress = None):
        self.adress = adress

class Email (Field):
    def __init__(self, mail = None):
        self.email = mail


class Record:
    def __init__(self, name, adress = None, phone = None, email = None, birthday = None):
        self.name = name
        self.adresses = []
        self.phones = []
        self.emails = []
        self.birthday = birthday
        if phone:
            self.phones.append(phone)
        if adress:
            self.adresses.append(adress)
        if email:
            self.emails.append(email)

    def add_adress(self, adress):
        self.adresses.append(adress)
        print(f"for {self.name} add adress {adress}.")

    def add_phone(self, phone):
        self.phones.append(phone)
        print(f"for {self.name} add phone {phone}.")

    def add_mail(self, mail):
        self.emails.append(mail)
        print(f"for {self.name} add mail {mail}.")

    def add_birthday(self, bd):
        self.birthday = bd
        print(f"{self.name} was born {bd}.")


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
