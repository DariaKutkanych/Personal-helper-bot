from collections import UserDict
from prettytable.colortable import ColorTable, Themes
import re


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
            print('\033[31m' + 'Номер не додано! Номер повинен містити не меньше 11 цифр')
            return


class Birthday(Field):
    pass


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
            print("\033[31m" + "Емейл не доданий не коректний формат! Формат excample@mail.com")
            return


class Record:
    pass


class Note(Field):
    pass


class NotesBook(UserDict):

    def __init__(self):
        self.data = []

    def add_note(self, note: Note):
        self.note = note.value
        self.added_note = {'id': '', 'tag': '', 'note': self.note}
        self.data.append(self.added_note)

    def menu_notes(self, action): # this def will change, when we will have finish

        while True:
            if (action == '1' or action == 'check') and self.data:
                print(self.data)
                break
            elif action == '2' or action == 'create':
                note = Note(input('Enter your notes: '))
                self.add_note(note)
                break
            elif action == '5' or action == 'exit':
                break
            else:
                print('You was wrong or notes didn\'t create')


class AddressBook(UserDict):

    def __init__(self):
        pass


class Menu:

    @property
    def main_menu(self):
        show_menu = ColorTable(theme=Themes.OCEAN)
        show_menu.field_names = [f"{18 * '-'}Меню{18 * '-'}"]
        show_menu.hrules = 1
        show_menu.align = "l"
        show_menu.add_rows([["1. Контакти"],
                            ["2. Нотатки"],
                            ["3. Іменниники"],
                            ["4. Сортувати папку"],
                            ["5. Вихід"],
                            ])
        return show_menu

    @property
    def main_contact(self):
        show_main_contact = ColorTable(theme=Themes.OCEAN)
        show_main_contact.field_names = [f"{18 * '-'}Контакти{18 * '-'}"]
        show_main_contact.hrules = 1
        show_main_contact.align = "l"
        show_main_contact.add_rows([["1. Створити контакт"],
                            ["2. Добавити дані до існуючого контакту"],
                            ["3. Редагувати дані контакту"],
                            ["4. Видалити дані з контакту"],
                            ["5. Повернутись в попереднє меню"],
                            ])
        return show_main_contact

    @property
    def add_menu(self):
        show_add_contact = ColorTable(theme=Themes.OCEAN)
        show_add_contact.field_names = [f"{18 * '-'}Що будем добавляти?{18 * '-'}"]
        show_add_contact.hrules = 1
        show_add_contact.align = "l"
        show_add_contact.add_rows([["1. Телефон"],
                                   ["2. Емейл"],
                                   ["3. Адресу"],
                                   ["4. День народження"],
                                   ["5. Повернутись в попереднє меню"]])
        return show_add_contact

    @property
    def edit_menu(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}Що будем редагувати?{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. Телефон"],
                              ["2. Емейл"],
                              ["3. Адресу"],
                              ["4. День народження"],
                              ["5. Повернутись в попереднє меню"]])
        return show_edit

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
    def notes_menu(self):
        show_notes_menu = ColorTable(theme=Themes.OCEAN)
        show_notes_menu.field_names = [f"{18 * '-'}Нотатки{18 * '-'}"]
        show_notes_menu.hrules = 1
        show_notes_menu.align = "l"
        show_notes_menu.add_rows([["1. Подивитись всі нотатки"],
                                      ["2. Додати нотатку"],
                                      ["3. Змінити нотатку"],
                                      ["4. Видалити нотатку"],
                                      ["5. Повернутись в попереднє меню"]])
        return show_notes_menu


class Handler:
    def __init__(self):
        self.menu = Menu()
        self.notes_book = NotesBook()
        self.address_book = AddressBook()

    def action_note(self, notes_book: NotesBook):
        self.notes_book = notes_book
        while True:
            print(self.menu.notes_menu)
            action = input("\033[34m" + "Обери потрібну команду(1-5), "
                                         "або я спробую вгадати: ")
            if (action == '1' or action == 'check') and  self.notes_book.data:
                print( self.notes_book.data)
            elif action == '2' or action == 'create':
                note = Note(input('Enter your notes: '))
                self.notes_book.add_note(note)
            elif action == '5' or action == 'exit':
                break
            else:
                print('You was wrong or notes didn\'t create')

    def action_phone(self, address_book: AddressBook):
        pass

    def main_action(self):
        while True:
            print(self.menu.main_menu)

            command = input("\033[34m" + "Обери потрібну команду(1-5), "
                                         "або я спробую вгадати: ")
            if command.lower() in ["exit", "close", "good bye", "5", "вихід", "выход"]:
                print("Good bye!")
                return 'break'
            elif command.lower() in ["нотатки", "note", "notes", "2",
                                     "замітки", "заметки"]:
                self.action_note(self.notes_book)
            elif command.lower() in ["phone", "номер телефона", "номер", "1"]:
                self.action_phone(self.address_book)


class Bot:

    def __init__(self):
        self.menu = Menu()  # should be changed
        self.handler = Handler()
        while True:
            if self.handler.main_action():
                break
            self.handler.main_action()

    def sort_files(self, file_name):
        # external sort func should be imported
        pass




if __name__ == "__main__":

    my_bot = Bot()
