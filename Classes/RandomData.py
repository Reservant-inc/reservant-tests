import random
import string

from faker import Faker
from datetime import datetime, timedelta


class RandomData:
    fake = Faker('pl_PL')

    # Metody generujące dane dla restauracji
    @staticmethod
    def generate_word():
        return RandomData.fake.word()

    @staticmethod
    def generate_address():
        return RandomData.fake.street_address()

    @staticmethod
    def generate_postal_code():
        return RandomData.fake.postcode()

    @staticmethod
    def generate_city():
        return RandomData.fake.city()

    @staticmethod
    def generate_nip():
        """Generuje poprawny numer NIP zgodnie z algorytmem walidacji."""
        while True:
            # Generujemy pierwsze 9 cyfr NIP
            nip_base = [random.randint(0, 9) for _ in range(9)]

            # Wagi do obliczeń
            weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]

            # Mnożymy cyfry przez odpowiednie wagi
            total = sum(nip_base[i] * weights[i] for i in range(9))

            # Obliczamy cyfrę kontrolną
            control_digit = total % 11

            # Kontrola, aby cyfra nie była 10 (nieprawidłowa)
            if control_digit != 10:
                nip_base.append(control_digit)
                return ''.join(map(str, nip_base))

    @staticmethod
    def generate_business_type():
        return random.choice(["Restaurant", "Bar", "Cafe"])

    @staticmethod
    def generate_description():
        return RandomData.fake.paragraph(nb_sentences=1)

    # Metody generujące dane dla pracownika
    @staticmethod
    def generate_first_name():
        return RandomData.fake.first_name()

    @staticmethod
    def generate_last_name():
        return RandomData.fake.last_name()

    @staticmethod
    def generate_login():
        return RandomData.fake.user_name()

    @staticmethod
    def generate_phone():
        return RandomData.fake.phone_number()

    @staticmethod
    def generate_password():
        length = 8  # Minimalna długość hasła

        # Definicja znaków, które muszą się znaleźć w haśle
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special_chars = "!@#$%^&*()"

        # Losowanie po jednym znaku z każdego typu
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(special_chars)
        ]

        # Wypełnienie reszty hasła losowymi znakami (aby osiągnąć minimalną długość 8 znaków)
        remaining_length = length - len(password)
        password += random.choices(lower + upper + digits + special_chars, k=remaining_length)

        # Tasowanie, aby znaki nie pojawiały się w przewidywalnym porządku
        random.shuffle(password)

        # Zwracanie jako string
        return ''.join(password)

    @staticmethod
    def generate_birth_date():
        return RandomData.fake.date_of_birth().strftime('%d.%m.%Y')

    # Metody generujące dane dla menu
    @staticmethod
    def generate_menu_type():
        return random.choice(["Food", "Alcohol"])

    @staticmethod
    def generate_menu_date_from():
        today = datetime.now()
        # dateFrom: losowa data między dziś a jutro
        date_from = today + timedelta(days=random.randint(0, 1))
        return date_from.strftime("%d%m%Y")

    @staticmethod
    def generate_menu_date_until():
        today = datetime.now()
        # dateUntil: losowa data między 30 dni a 60 dni od dziś
        date_until = today + timedelta(days=random.randint(30, 60))
        return date_until.strftime("%d%m%Y")

    # Dodatkowe metody generujące
    @staticmethod
    def generate_email():
        return RandomData.fake.email()

    @staticmethod
    def generate_paragraph():
        return RandomData.fake.paragraph(nb_sentences=1)

    @staticmethod
    def generate_tags(n=3):
        # Lista przykładowych tagów
        possible_tags = ['Italian', 'Mexican', 'Chinese', 'Vegetarian', 'Seafood', 'Fast Food']
        return random.sample(possible_tags, n)
