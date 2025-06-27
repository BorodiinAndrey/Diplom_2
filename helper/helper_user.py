from faker import Faker


def create_fake_email():
    fake = Faker()
    return fake.email()

def create_fake_password():
    fake = Faker()
    return fake.password()

def create_fake_name():
    fake = Faker()
    return fake.name()

