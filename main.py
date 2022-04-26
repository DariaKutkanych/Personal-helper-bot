from collections import UserDict
from sort_files import sort_folder
from prettytable.colortable import ColorTable, Themes
import datetime
import re


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
        elif type(value) == datetime.datetime:
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

    @Field.value.setter
    def value(self, add_value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, add_value)):
            Field.value.fset(self, add_value)
        else:
            print("\033[31m" + "Емейл не доданий не коректний формат! Формат excample@mail.com")
            return


class Adress(Field):
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
        self.birthday = Birthday(bd)
        print(f"{self.name} was born {bd}.")
        
    def change_adress(self, new_adres, old_adres):
        adress_list = []
        for a.value in self.adresses:
            adress_list.append(str(a.value))
        if old_adres in adress_list:
            old_adress = Adress(old_adres)
            self.adresses.remove(old_adress)
            new_adress = Adress(new_adres)
            self.adresses.append(new_adress)
        else:
            print(f"This adress {old_adres} is not in the list")
            
    def change_phone(self, new_num, old_num):
        phone_list = []
        for p.value in self.phone:
            phone_list.append(str(p.value))
        if old_num in phone_list:
            old_phone = Phone(old_num)
            self.phones.remove(old_phone)
            new_phone = Phone(new_num)
            self.phones.append(new_phone)
        else:
            print(f"This phone {old_num} is not in the list")
            
    def change_email(self, new_email, old_email):
        email_list = []
        for p.value in self.email:
            email_list.append(str(p.value))
        if old_email in email_list:
            old_mail = Email(old_email)
            self.emails.remove(old_mail)
            new_mail = Email(new_email)
            self.emails.append(new_mail)
        else:
            print(f"This email {old_email} is not in the list")
            
    def change_birthday(self, new_birthday, old_birthday):
        if self.birthday == old_birthday:
            self.birthday = new_birthday
         
    def delete_number(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except:
            NameError("Number not listed")
    
    def delete_mail(self, mail: Email):
        try:
            self.emails.remove(mail)
        except:
            NameError("Email not listed")
        
    def delete_adress(self, adress: Adress):
        try:
            self.adresses.remove(adress)
        except:
            NameError("Adress not listed")



class NotesBook(UserDict):

    def __init__(self):
        self.data = []

    def add_note(self, note: Note):
        self.note = note.value
        self.added_note = {'id': len(self.data)+1, 'tag': '', 'note': \
            self.note}
        self.data.append(self.added_note)
        flag_tag = input("Do you want to add tag for this note? Enter y, "
                         "if yes otherwise enter n")

    def search_note(self):
        pass


class AddressBook(UserDict):

#    def __init__(self):  Comment it. With this func AddressBook has no atribut data
#        pass
    def add_record(self, set):
        if isinstance(set, Record):
            self.data.__setitem__(set.name, (set.adresses, set.phones, set.emails, set.birthday))
        else:
            print("try add Record.")
            
    def get_bd(self, day):
        now = datetime.datetime.now()                                                           
        delta = now + datetime.timedelta(days = day)
        birthday_people = [] 
        for k, v in self.data.items():
            for el in v:
                if isinstance(el, Birthday):
                    date_val = (el.value).replace(year = now.year)
                    if now < date_val.replace(hour=23, minute=59, second=59, microsecond=0) < delta:
                        birthday_people.append(k)
        print (birthday_people)
<<<<<<< HEAD
    def search_by_name(self, name):
        pass
=======
>>>>>>> 54024ed99a571d7a280f7edfd5e28e95a079d7c7


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
                                      ["6. Повернутись в попереднє меню"]])
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
                #self.notes_book.add_note(note)
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

            if command.lower() in ["exit", "close", "good bye", "5", "вихід", "выход"]:
                print("Good bye!")
                break
                
            elif command.lower() in ["нотатки", "note", "notes", "2",
                                     "замітки", "заметки"]:
                self.action_note(self.notes_book)
            elif command.lower() in ["phone", "телефон", "номер", "1","number"]:
                self.action_phone(self.address_book)


class Bot:

    def __init__(self):
        self.menu = Menu()  # should be changed
        self.handler = Handler()
        self.handler.main_action()

    def sort_files(self, file_path):
        sort_folder(file_path)


if __name__ == "__main__":

    my_bot = Bot()


