from collections import UserDict
from prettytable.colortable import ColorTable, Themes


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
    def change_menu(self):
        show_change_contact = ColorTable(theme=Themes.OCEAN)
        show_change_contact.field_names = [f"{18 * '-'}Що будем змінювати?{18 * '-'}"]
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
