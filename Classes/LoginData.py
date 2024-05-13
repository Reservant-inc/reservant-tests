from faker import Faker
from faker.decode import unidecode
from utils.utils import get_variable_value


class LoginData:
    def __init__(self, first_name, last_name, login, email, phone_number, birth_day, password):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.email = email
        self.phone_number = phone_number
        self.birth_day = birth_day
        self.password = password

    def __str__(self):
        return (f"LoginData(first_name={self.first_name}, last_name={self.last_name}, "
                f"login={self.login}, email={self.email}, phone_number={self.phone_number}, "
                f"birth_day={self.birth_day}, password={self.password})")

    @staticmethod
    def generate_login_data():
        fake = Faker('pl_PL')
        first_name = fake.first_name()
        last_name = fake.last_name()
        login = unidecode(first_name).lower()[:3] + unidecode(last_name).lower()[:3]
        email = fake.email()
        phone_number = fake.phone_number().replace(' ', '')[-9:]
        birth_day = fake.date_of_birth().strftime('%d.%m.%Y')
        password = get_variable_value("TEST_PASSWORD")

        return LoginData(first_name, last_name, login, email, phone_number, birth_day, password)
