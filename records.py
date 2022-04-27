from field import Name, Phone, Email, Address, Birthday


class Record:

    def __init__(self, name, address=None, phone=None, email=None, birthday=None):

        self.name = name if name.value else None
        self.addresses = []
        self.phones = []
        self.emails = []
        self.birthday = birthday

    def add_address(self, address=None):
        if address:
            address_list = []
            for address in self.addresses:
                address_list.append(str(address.value))
            if address in address_list:
                print("This address has alredy been added.")
            else:
                new_address = Address(address)
                self.addresses.append(new_address)
                print(f"for {self.name} add address {address}.")
        else:
            print("You didn't write an adress.")
            a = input("Please enter address. ")
            self.add_address(a)

    def add_phone(self, phone):
        phones_list = []
        for phone in self.phones:
            phones_list.append(str(phone.value))
        if phone in phones_list:
            print("This num has already been added.")
        else:
            new_phone = Phone(phone)
            self.phones.append(new_phone)
            print(f"for {self.name} add phone {new_phone}.")

    def add_mail(self, mail):
        mail_list = []
        for email in self.emails:
            mail_list.append(str(email.value))
        if mail in mail_list:
            print("This mail has alredy been added.")
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
