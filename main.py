from collections import UserDict
from prettytable.colortable import ColorTable, Themes
import re
from datetime import datetime

class AddressBook(UserDict):

#    def __init__(self):  Comment it. With this func AddressBook has no atribut data
#        pass
    def add_record(self, set):
        if isinstance(set, Record):
            self.data.__setitem__(set.name, (set.adresses, set.phones, set.emails, set.birthday))
        else:
            print("try add Record.")

class Field:

    def __init__(self, value):
        self.__value = Name
        self.value = value

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

    def __init__(self, phone=None):
        self.phone = phone

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, new_value):
        if len(list(new_value)) >= 11:
            self.phone = new_value
        else:
            print(
                '\033[31m' + 'Номер не додано! Номер повинен містити не меньше 11 цифр')
            return


class Birthday(Field):
    def __init__(self, birthday_d = None, birthday_m = None, birthday_y = None):
        try:
            self.birthday = datetime(birthday_y, birthday_m, birthday_d)
        except:
            self.birthday = None
            print("Enter birthday date in next form: dd, mm, yyyy!")


class Email(Field):

    def __init__(self, mail=None):
        self.email = mail

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, add_value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, add_value)):
            self.email = add_value
        else:
            print(
                "\033[31m" + "Емейл не доданий не коректний формат! Формат excample@mail.com")
            return

class Adress(Field):
    pass

class Email(Field):
    pass



class Record:
    def __init__(self, name, adress = None, phone = None, email = None, birthday = None):
        if isinstance (name, Name):
            self.name = name
        self.adresses = []
        self.phones = []
        self.emails = []
        self.birthday = birthday

    def add_adress(self, adress):
        adress_list = []
        for a.value in self.adresses:
            adress_list.append(str(a.value))
        if adress in adress_list:
            print("This adress alredy been added.") 
        else:
            new_adress = Adress(adress)
            self.adresses.append(adress)
            print(f"for {self.name} add adress {adress}.")

    def add_phone(self, phone):
        phones_list = []
        for p.value in self.phones:
            phones_list.append(str(p.value))
        if phone in phones_list:
            print("This num alredy been added.")
        else:
            new_phone = Phone(phone)
            self.phones.append(new_phone)
            print(f"for {self.name} add phone {new_phone}.")

    def add_mail(self, mail):
        mail_list = []
        for m.value in self.emails:
            mail_list.append(str(m.value))
        if mail in mail_list:
            print("This mail alredy been added.") 
        else:
            new_mail = Email(mail)
            self.emails.append(new_mail)
            print(f"for {self.name} add mail {mail}.")

    def add_birthday(self, bd):
        self.birthday = bd
        print(f"{self.name} was born {bd}.")


class Notes:
    pass


class NotesBook(UserDict):

    def __init__(self):
        self.data = []

    def add_note(self, note: Notes):
        added_note = {'id': '', 'tag': '', 'note': note}
        self.data.append(added_note)

    def print_menu(self):
        while True:
            command = input('''Do you want create notes or check?
                            Create: enter 1 or create
                            Check: enter 2 or check
                            If you need exit, enter exit or 0\n''').lower()
            if command == '1' or command == 'create':
                note = Notes(input('Enter your notes: '))
                self.add_note(note)
            elif command == '2' or command == 'check':
                print(self.data)
            elif command == '0' or command == 'exit':
                break


class Menu:

    @property
    def main_menu(self):
        show_menu = ColorTable(theme=Themes.OCEAN)
        show_menu.field_names = [f"{18 * '-'}Меню{18 * '-'}"]
        show_menu.hrules = 1
        show_menu.align = "l"
        show_menu.add_rows([["1. Створити новий контакт"],
                            ["2. Добавити дані до існуючого контакту"],
                            ["3. Видалити дані з контакту"],
                            ["4. Змінити дані контакту"],
                            ["5. Іменниники"],
                            ["6. Посторінковий вивід контактної книги"],
                            ["7. Пошук по контактній книзі"],
                            ["8. Показати всі контакти"],
                            ["9. Нотатки"],
                            ["10. Сортувати папку"],
                            ["11. Вихід"],
                            ])
        return show_menu

    @property
    def delete_menu(self):
        show_delete = ColorTable(theme=Themes.OCEAN)
        show_delete.field_names = [f"{18 * '-'}Що будем видаляти?{18 * '-'}"]
        show_delete.hrules = 1
        show_delete.align = "l"
        show_delete.add_rows([["1. Телефон"],
                              ["2. Емейл"],
                              ["3. Адресу"],
                              ["4. День народження"],
                              ["5. Видалити контакт з книги"],
                              ["6. Повернутись в попереднє меню"]])
        return show_delete

    @property
    def add_menu(self):
        show_add_contact = ColorTable(theme=Themes.OCEAN)
        show_add_contact.field_names = [
            f"{18 * '-'}Що будем добавляти?{18 * '-'}"]
        show_add_contact.hrules = 1
        show_add_contact.align = "l"
        show_add_contact.add_rows([["1. Телефон"],
                                   ["2. Емейл"],
                                   ["3. Адресу"],
                                   ["4. День народження"],
                                   ["5. Повернутись в попереднє меню"]])
        return show_add_contact

    @property
    def change_menu(self):
        show_change_contact = ColorTable(theme=Themes.OCEAN)
        show_change_contact.field_names = [
            f"{18 * '-'}Що будем змінювати?{18 * '-'}"]
        show_change_contact.hrules = 1
        show_change_contact.align = "l"
        show_change_contact.add_rows([["1. Телефон"],
                                      ["2. Емейл"],
                                      ["3. Адресу"],
                                      ["4. День народження"],
                                      ["5. Повернутись в попереднє меню"]])
        return show_change_contact


class Bot:

    def __init__(self):

        self.Adderessbook = AddressBook()
        self.notes = []  # a func add_note should create an instance of Note
        # and add it to current list
        self.menu = Menu()  # should be changed

        while True:
            print(self.menu.main_menu)
            command = input("I am waiting for your command: ")

            if command.lower() in ["exit", "close", "good bye", "11", "вихід", "выход"]:
                print("Good bye!")
                break

    def sort_files(self, file_name):
        # external sort func should be imported
        pass


if __name__ == "__main__":

    my_bot = Bot()
