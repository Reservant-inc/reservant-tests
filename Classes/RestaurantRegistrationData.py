import random
from faker import Faker

class RestaurantRegistrationData:
    def __init__(self, name, address, postal_code, city, nip, business_type, description):
        self.name = name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.nip = nip
        self.business_type = business_type
        self.description = description

    def __str__(self):
        return (f"RestaurantRegistrationData(name={self.name}, address={self.address}, "
                f"postal_code={self.postal_code}, city={self.city}, nip={self.nip}, "
                f"business_type={self.business_type}, description={self.description})")

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
    def generate_restaurant_data():
        fake = Faker('pl_PL')

        # Generowanie danych restauracji
        name = fake.company()
        address = fake.street_address()
        postal_code = fake.postcode()
        city = fake.city()
        nip = RestaurantRegistrationData.generate_nip()

        # Losowanie typu działalności
        business_type = random.choice(["Restaurant", "Bar", "Cafe"])

        description = fake.paragraph(nb_sentences=1)

        return RestaurantRegistrationData(name, address, postal_code, city, nip, business_type, description)
