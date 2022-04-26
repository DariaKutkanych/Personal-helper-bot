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
            new_address = Address(address)
            self.addresses.append(address)
            print(f"for {self.name} add address {address}.")

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
        
    def change_adress(self, new_adres, old_adres):
        adress_list = []
        for a in self.adresses:
            adress_list.append(str(a.value))
        if adress_list == [] or self.address == None:
            print("The list is empty")
        if old_adres in adress_list:
            old_adress = Address(old_adres)
            self.adresses.remove(old_adress)
            new_adress = Address(new_adres)
            self.adresses.append(new_adress)
        else:
            print(f"This adress {old_adres} is not in the list")
            
    def change_phone(self, new_num, old_num):
        phone_list = []
        for p in self.phone:
            phone_list.append(str(p.value))
        if phone_list == [] or self.phone == None:
            print("The list is empty")
        if old_num in phone_list:
            old_phone = Phone(old_num)
            self.phones.remove(old_phone)
            new_phone = Phone(new_num)
            self.phones.append(new_phone)
        else:
            print(f"This phone {old_num} is not in the list")
            
    def change_email(self, new_email, old_email):
        email_list = []
        for p in self.email:
            email_list.append(str(p.value))
        if email_list == [] or self.email == None:
            print("The list is empty")
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
        
    def delete_adress(self, adress: Address):
        try:
            self.adresses.remove(adress)
        except:
            NameError("Adress not listed")
