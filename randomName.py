
from email.headerregistry import Address
from faker import Faker

fake = Faker()
name = "Name : "+ fake.name()
address = "Address : " + fake.address()

print(name,address)
