
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
    NO_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

class Ingredients:
    BUN = '61c0c5a71d1f82001bdaaa6d'
    MEAT = '61c0c5a71d1f82001bdaaa6f'
    SAUCE = '61c0c5a71d1f82001bdaaa72'

