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

    def get_bd(self, day):
        now = datetime.datetime.now()
        delta = now + datetime.timedelta(days=day)
        birthday_people = []
        for k, v in self.data.items():
            for el in v:
                if isinstance(el, Birthday):
                    date_val = (el.value).replace(year=now.year)
                    if now < date_val.replace(hour=23, minute=59, second=59, microsecond=0) < delta:
                        birthday_people.append(k)
        print(birthday_people)
        
    def search_by_name(self, surname):
        for i in self.data.name:
            if i.value == surname:
                return self.data[self.data.name.index(surname)]
        return f"There is no contact with this name"
    
    def search_by_phone(self, number):
        for i in self.data.phone:
            if i.value == number:
                return self.data[self.data.phone.index(number)]
        return f"There is no contact with this phone"
    
    def search_by_email(self, mail):
        for i in self.data.emails:
            if i.value == mail:
                return self.data[self.data.emails.index(mail)]
        return f"There is no contact with this email"
    
    def search_by_address(self, adres):
        for i in self.data.addresses:
            if i.value == adres:
                return self.data[self.data.addresses.index(adres)]
        return f"There is no contact with this email"
        
