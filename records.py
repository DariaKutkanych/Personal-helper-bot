from field import Name, Phone, Email, Address, Birthday


class Record:

    def __init__(self, name, address=None, phone=None, email=None, birthday=None):
        if isinstance(name, Name):
            self.name = name
        self.addresses = []
        self.phones = []
        self.emails = []
        self.birthday = birthday

    def add_address(self, address):
        address_list = []
        for a in self.addresses:
            address_list.append(str(a.value))
        if address in address_list:
            print("This address alredy been added.")
        else:
            print("You don't write adress.")
            a = input("Please enter address. ")
            self.add_address(a)

    def add_phone(self, phone):
        phones_list = []
        for p in self.phones:
            phones_list.append(str(p.value))
        if phone in phones_list:
            print("This num alredy been added.")
        else:
            new_phone = Phone(phone)
            self.phones.append(new_phone)
            print(f"for {self.name} add phone {new_phone}.")

    def add_mail(self, mail):
        mail_list = []
        for m in self.emails:
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
        
    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
