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

class FakeHuman:
    payload = {
        "email": "uniqueemail109@domain.com",
        "password": "uniquepassword109",
        "name": "uniquename109"
    }

class APIResponses:
    USER_DUPLICATE = {
        "message": "User already exists",
        "success": False
    }
    USER_MISSING = {
        "message": "Email, password and name are required fields",
        "success": False
    }
    USER_MALFORMED = {
        "success": False,
        "message": "email or password are incorrect"
    }
    USER_NO_AUTH = {
        "success": False,
        "message": "You should be authorised"
    }

