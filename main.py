from addressbook import AddressBook
from field import Note
from sort_files import sort_folder
from prettytable.colortable import ColorTable, Themes
from notes import NotesBook


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
            if action.lower() in ["1", "check", "подивитись", "нотатки",
                                  "замітки", "заметки"]:
                print(self.notes_book.data)
            elif action.lower() in ["2", "create", "створити", "создать",
                                    "замітки", "заметки"]:
                note = Note(input('Введіть нонатку: '))
                self.notes_book.add_note(note)
            elif action.lower() in ["3", "знайти", "search", "нотатки",
                                    "замітки", "заметки"]:
                pass
                # self.notes_book.add_note(note)
            elif action.lower() in ["exit", "close", "good bye", "5", "вихід",
                                    "выход"]:
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
            user_text = set()
            for el in command.split(' '):
                user_text.add(el.lower())

            contact = {"1", "1.", "контакт", "контакты", "контакти", "contact"}
            notes = {"2", "2.", "нотатки", "нотаткы", "notes", "нотатку", "замітки", "заметки"}
            birthday = {"3", "3.", "іменниники", "імениники", "birthday", "народження", "рождения"}
            sort = {"4", "4.", "сортувати", "sorted", "відсортувати", "посортувати", "сортировка", "sort"}
            close = {"5", "5.", "закрити", "вийти", "exit", "close", "good bye", "вихід", "выход", "завершити"}

            if len(user_text & contact) >= 1:
                self.action_phone(self.address_book)

            elif len(user_text & notes) >= 1:
                self.main_action_note(self.notes_book)
            elif len(user_text & birthday) >= 1:
                pass
            elif len(user_text & sort) >= 1:
                 pass
            elif len(user_text & close) >= 1:
                print("Good bye!")
                break
            else:
                print("Я Вас не зрозумів:(\nСпробуйте ще раз!")


class Bot:

    def __init__(self):
        self.menu = Menu()  # should be changed
        self.handler = Handler()
        self.handler.main_action()

    def sort_files(self, file_path):
        sort_folder(file_path)


if __name__ == "__main__":

    my_bot = Bot()
