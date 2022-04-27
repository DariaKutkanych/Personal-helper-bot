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
        if day:
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
