from faker import Faker
class EmployeeRegistrationData:

    def __init__(self, first_name, last_name, login, phone, password, password_confirmation):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.phone = phone
        self.password = password
        self.password_confirmation = password_confirmation

    @staticmethod
    def generate_employee_data():
        fake = Faker('pl_PL')

        # Generowanie danych pracownika
        first_name = fake.first_name()
        last_name = fake.last_name()
        login = fake.user_name()
        phone = fake.phone_number()
        password = fake.password()
        # ?password_confirmation = password
        password_confirmation = password

        return EmployeeRegistrationData(first_name, last_name, login, phone, password, password_confirmation)
