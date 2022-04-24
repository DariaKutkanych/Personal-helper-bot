from collections import UserDict
import datetime
from prettytable.colortable import ColorTable, Themes
import re


class AddressBook(UserDict):

    def __init__(self):
        pass


class Field:

    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) == str:
            self.__value = value


class Name(Field):
    pass


class Phone(Field):

    @Field.value.setter
    def value(self, new_value):
        if len(list(new_value)) >= 11:
            Field.value.fset(self, new_value)
        else:
            print('\033[31m' + 'Номер не додано! Номер повинен містити не меньше 11 цифр')


class Birthday(Field):

    @Field.value.setter
    def value(self, new_value):
        if len(list(new_value)) == 10 and \
                int(new_value[0:4]) > 0 and \
                int(new_value[5:7]) > 0 and \
                int(new_value[8:10]) > 0:
            Field.value.fset(self, new_value)
        else:
            print('\033[31m' + 'Некоректний формат дати! Потрібний формам ррр-мм-дд. Дата не додана')


class Email(Field):

    @Field.value.setter
    def value(self, add_value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, add_value)):
            Field.value.fset(self, add_value)
        else:
            print("\033[31m" + "Емейл не доданий не коректний формат! Формат excample@mail.com")


class Record:
    pass


class Notes:
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


class Bot:

    def __init__(self):

        self.Adderessbook = AddressBook()
        self.notes = []  # a func add_note should create an instance of Note
        # and add it to current list
        self.menu = Menu()  # should be changed

        while True:
            print(self.menu.main_menu)

            command = input("\033[34m" + "Обери потрібну команду(1-5), або я спробую вгадати: ")

            if command.lower() in ["exit", "close", "good bye", "5", "вихід", "выход"]:
                print("Good bye!")
                break

    def sort_files(self, file_name):
        # external sort func should be imported
        pass


if __name__ == "__main__":

    my_bot = Bot()

