from addressbook import AddressBook
from field import Note
from sort_files import sort_folder
from prettytable.colortable import ColorTable, Themes
from notes import NotesBook
from notes import RecordNote


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
                                  ["3. Знайти нотатку"],
                                  ["4. Змінити нотатку"],
                                  ["5. Видалити нотатку"],
                                  ["6. Сортувати нотатки за тегами"],
                                  ["7. Повернутись в попереднє меню"]])
        return show_notes_menu


    @property
    def search_note(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}За яким критерієм будемо шукати?"
                                 f"{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. По id замітки"],
                            ["2. По тегу замітки"],
                            ["3. По головному слову"],
                            ["4. Повернутись в попереднє меню"]])
        return show_edit


class Handler:

    def __init__(self, notes_book: NotesBook, address_book: AddressBook):
        self.menu = Menu()
        self.notes_book = notes_book
        self.address_book = address_book
        self.main_action()

    def main_action_note(self, notes_book: NotesBook):
        while True:
            print(self.menu.notes_menu)
            action = input("\033[34m" + "Обери потрібну команду(1-5), "
                                        "або я спробую вгадати: ")
            if action.lower() in ["1", "check", "подивитись"]:
                self.notes_book.print_note_book()
            elif action.lower() in ["2", "create", "створити", "создать"]:
                record_note = RecordNote()
                record_note.add_note(Note(input('Введіть нонатку: '
                                                           '')))
                flag_tag = input("Чи хочете ви додати тег до замітки? Введіть "
                                 "так, якщо бажаєте, інакше ні: ")
                if flag_tag.lower() in ["так", "yes", "да", "хочу"]:
                    record_note.add_tag(input('Введіть тег: '))
                self.notes_book.add_record_note(record_note)
            elif action.lower() in ["3", "знайти", "search", "пошук", "найти"]:
                self.notes_book.print_note_book(self.action_search_note(
                    notes_book))

            elif action.lower() in ["4", "edit", "редагувати", "змінити",
                                    "изменить"]:
                pass
            elif action.lower() in ["5", "delete", "remove", "видалити",
                                    "удалить", "стерти"]:
                del_notes = self.action_search_note(notes_book)
                print(f"Ви намагаєтесь видалити замітки:\n ")
                self.notes_book.print_note_book.del_notes
                flag_notes_delete = input("Якщо хочете видалити, напишіть"
                                          " + або так, для безпеки видаляйте "
                                          "за id: ")
                if flag_notes_delete.lower() in ["+", "так", "хочу", "го",
                                                 "yes"]:
                    self.notes_book.delete_note(del_notes)
                    print("Успішно видалено!")
            elif action.lower() in ["сортувати", "sort", "сортування", "6",
                                    "сортировка"]:
                self.notes_book.sort_note()
            elif action.lower() in ["exit", "close", "good bye", "7", "вихід",
                                    "выход", "повернутись"]:
              
                break
            else:
                print("Ви помилились або нотаток немає")

    def action_search_note(self, notes_book: NotesBook):
        while True:
            print(self.menu.search_note)

            command = input("\033[34m" + "Обери потрібну команду(1-4), "
                                         "або я спробую вгадати: ")
            if command.lower() in ["id", "ид", "ід", "1"]:
                id_parametr = input('Введіть id нотатки: ').lower()
                return notes_book.search_parametr_note("id", id_parametr)
            elif command.lower() in ["tag", "тег", "notes", "2"]:
                tag_parametr = input('Введіть tag нотатки: ').lower()
                return notes_book.search_parametr_note("tag", tag_parametr)
            elif command.lower() in ["головне", "main", "слово", "3"]:
                word_parametr = input('Введіть головне слово нотатки: ')
                return notes_book.search_word_note(word_parametr)
            elif command.lower() in ["exit", "close", "good bye", "4",
                                     "вихід", "выход", "повернутись"]:
                print("Good bye!")
                break

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
                # Dasha this need changes
                file_path = input('Введіть шлях до файлу')
                sort_folder(file_path)

            elif len(user_text & close) >= 1:
                print("Good bye!")
                break
            else:
                print("Я Вас не зрозумів:(\nСпробуйте ще раз!")


class Bot:

    def __init__(self):
        self.menu = Menu()
        self.notes_book = NotesBook()
        self.address_book = AddressBook()
        self.handler = Handler(self.notes_book, self.address_book)


if __name__ == "__main__":

    my_bot = Bot()