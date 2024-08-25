from faker import Faker

class RealHumans:
    @staticmethod
    def create_real_human():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.firstname()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

class FakeHuman:
    payload = {
        "email": "uniqueemail109@domain.com",
        "password": "uniquepassword109",
        "name": "uniquename109"
    }
