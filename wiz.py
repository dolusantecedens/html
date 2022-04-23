

from faker import Faker
fake = Faker()
class BaseContact:
    def __init__(self, name, surname, email, phone_num):
        self.name=name
        self.surname=surname
        self.phone_num=phone_num
        self.email=email
        self.length=len(name)+len(surname)
    def __str__ (self):
        return f'{self.surname} {self.name} {self.email} {self.phone_num}'
    def contact(self, name, surname, phone_num):
        print(f'wybieram numer {phone_num} i dzwonie do {name}{surname}')
class BusinessContact(BaseContact):
    def __init__(self, business_num, company, position, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.business_num=business_num
        self.company=company
        self.position=position
    def contact(self, name, surname, business_num):
        print(f'wybieram numer {business_num} i dzwonie do {name}{surname}')
def create_contacts(type,amount):
    fakeBase=[]
    if type=='BaseContact':
        for i in range(amount):
            i=BaseContact(name=fake.first_name(),surname=fake.last_name(),email=fake.email(),phone_num=fake.phone_number())
            fakeBase.append(i)
    else:
        for i in range(amount):
            i=BusinessContact(name=fake.first_name(),surname=fake.last_name(),email=fake.email(),phone_num=fake.phone_number(),position=fake.job(),business_num=fake.phone_number(),company=fake.company())
            fakeBase.append(i)
    return fakeBase
x=create_contacts('x',5)
print(x[3])