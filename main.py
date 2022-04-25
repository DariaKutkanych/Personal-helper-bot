from collections import UserDict, UserList
from prettytable.colortable import ColorTable, Themes
import re


class Field:

    def __init__(self, value):
        self.__value = None
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) == str:
            self.__value = value
        elif type(value) == datetime.datetime:
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

    @Field.value.setter
    def value(self, new_value):
        try:
            birthday = datetime.datetime.strptime(new_value, '%Y-%m-%d')
            Field.value.fset(self, birthday)
        except ValueError:
            print('\033[31m' + 'Некоректний формат дати! Потрібний формам ррр-мм-дд. Дата не додана')


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


class NotesBook(UserList):

    def __init__(self):
        self.data = []
        self.note = ""
        self.id_note = None
        self.tag = ""

    def __str__(self):
        #need to add beautiful output like in future AddressBook
        return f"{self.data}"

    def add_note(self, note: Note, tag = ""):
        self.note = note
        self.tag = tag
        self.id_note = len(self.data)+1
        self.data.append({"id": self.id_note, "tag": self.tag,
                               "note": self.note})

    def delete_note(self, note: Note):
        for i in self.data:
            if i.get('note') == note:
                return (f"Вы удалили заметку {self.data.pop(self.data.index(i))}")

    def search_parametr_note(self, note_parametr, user_parametr):
        for i in self.data:
            if str(i.get(note_parametr)) == user_parametr:
                return i.get("note")

    def search_word_note(self, part_note): #need to be impoves
        self.find_all_notes = []
        for i in self.data:
            if re.findall(part_note, str(i.get('note'))):
                self.find_all_notes.append(i.get('note'))
        return self.find_all_notes

    def edit_note(self, note: Note):
        pass

    def sort_note(self):
        pass


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
                                      ["3. Знайти нотатку"],
                                      ["4. Змінити нотатку"],
                                      ["5. Видалити нотатку"],
                                      ["6. Сортувати нотатки за тегами"],
                                      ["7. Повернутись в попереднє меню"]])
        return show_notes_menu

    @property
    def search_note(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}За яким критерієм?"
                                 f"{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. По id замітки"],
                              ["2. По тегу замітки"],
                              ["3. По головному слову"],
                              ["4. Повернутись в попереднє меню"]])
        return show_edit

    @property
    def edit_note(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}Що змінити?"
                                 f"{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. Тег"],
                              ["2. нотатку"],
                              ["3. Повернутись в попереднє меню"]])
        return show_edit


class Handler:
    def __init__(self, notes_book : NotesBook, address_book: AddressBook):
        self.menu = Menu()
        self.notes_book = notes_book
        self.address_book = address_book

    def main_action_note(self, notes_book: NotesBook):
        self.notes_book = notes_book
        while True:
            print(self.menu.notes_menu)
            action = input("\033[34m" + "Обери потрібну команду(1-5), "
                                         "або я спробую вгадати: ")
            if action.lower() in ["1", "check", "подивитись"]:
                print(notes_book)
            elif action.lower() in ["2", "create", "створити", "создать"]:
                note = Note(input('Введіть нонатку: '))
                flag_tag = input("Чи хочете ви додати тег до замітки? Введіть "
                              "так, якщо бажаєте, інакше ні: ")
                if flag_tag.lower() in ["так", "yes", "да", "хочу"]:
                    tag_note = Note(input('Введіть тег: '))
                    self.notes_book.add_note(note, tag_note)
                else:
                    self.notes_book.add_note(note)
            elif action.lower() in ["3", "знайти", "search", "пошук", "найти"]:
                print(self.action_search_note(notes_book))
            elif action.lower() in ["4", "edit", "редагувати", "змінити",
                                    "изменить"]:
                pass
            elif action.lower() in ["5", "delete", "remove", "видалити",
                                    "удалить", "стерти"]:
                print(self.notes_book.delete_note(self.action_search_note(
                    notes_book)))
            elif action.lower() in ["exit", "close", "good bye", "6", "вихід",
                                    "выход","повернутись"]:
                break
            else:
                print('You was wrong or notes didn\'t create')

    def action_search_note(self, notes_book: NotesBook):
        while True:
            print(self.menu.search_note)

            command = input("\033[34m" + "Обери потрібну команду(1-4), "
                                         "або я спробую вгадати: ")
            if command.lower() in ["id", "ид", "ід", "1"]:
                id_parametr = input('Введіть id нотатки: ')
                return notes_book.search_parametr_note("id", id_parametr)
            elif command.lower() in ["tag", "тег", "notes", "2"]:
                tag_parametr = input('Введіть tag нотатки: ')
                return notes_book.search_parametr_note("tag", tag_parametr)
            elif command.lower() in ["головне", "main", "слово", "3"]:
                word_parametr = input('Введіть головне слово нотатки: ')
                return notes_book.search_word_note(word_parametr)
            elif command.lower() in ["exit", "close", "good bye", "4",
                                     "вихід", "выход", "повернутись"]:
                print("Good bye!")
                break

    def action_edit_note(self, notes_book: NotesBook):
        pass

    def action_phone(self, address_book: AddressBook):
        pass

    def main_action(self):
        while True:
            print(self.menu.main_menu)

            command = input("\033[34m" + "Обери потрібну команду(1-5), "
                                         "або я спробую вгадати: ")
            if command.lower() in ["exit", "close", "good bye", "5", "вихід", "выход"]:
                print("Good bye!")
                break

            elif command.lower() in ["нотатки", "note", "notes", "2",
                                     "замітки", "заметки"]:
                self.main_action_note(self.notes_book)
            elif command.lower() in ["phone", "телефон", "номер", "1","number"]:
                self.action_phone(self.address_book)


class Bot:

    def __init__(self):
        self.menu = Menu()
        self.notes_book = NotesBook()
        self.address_book = AddressBook()
        self.handler = Handler(self.notes_book, self.address_book)

        while True:
            if self.handler.main_action() is None:
                break
            self.handler.main_action()


    def sort_files(self, file_name):
        # external sort func should be imported
        pass


if __name__ == "__main__":
    my_bot = Bot()
    