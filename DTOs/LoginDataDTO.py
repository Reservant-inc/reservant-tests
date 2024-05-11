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
