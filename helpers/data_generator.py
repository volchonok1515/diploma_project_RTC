import random
import string


class DataGenerator:
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits

    @property
    def get_email(self):
        user_name = ''.join(random.choice(self.lower_letters) for _ in range(10))
        return f'{user_name}_test@gmail.com'

    @property
    def get_password(self):
        return ''.join(random.choice(self.lower_letters + self.upper_letters + self.digits) for _ in range(18))