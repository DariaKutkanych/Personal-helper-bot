import datetime
from collections import UserDict
from records import Record, Birthday, Address, Name, Phone


class AddressBook(UserDict):

    def add_record(self, set):
        if isinstance(set, Record):
            self.data.__setitem__(
                set.name, (set.addresses, set.phones, set.emails, set.birthday))
        else:
            print("try add Record.")


    def get_bd(self, day=None):
        if day.isdigit():
            now = datetime.datetime.now()
            delta = now + datetime.timedelta(days=int(day))
            birthday_people = []
            for k, v in self.data.items():
                for el in v:
                    if isinstance(el, Birthday):
                        date_val = (el.value).replace(year=now.year)
                        if now < date_val.replace(hour=23, minute=59, second=59, microsecond=0) < delta:
                            birthday_people.append(k)
            print(birthday_people)
        else:
            d = input("Enter for what period to show birthdays: ")
            self.get_bd(d)

    def search_by_name(self, surname):
        pass

    def search_by_phone(self, number):
        pass

    def search_by_email(self, mail):
        pass

    def search_by_address(self, adres):
        pass

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
