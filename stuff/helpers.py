from faker import Faker

class RealHumans:
    @staticmethod
    def create_real_human():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.first_name()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload