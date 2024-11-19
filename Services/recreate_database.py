import requests

class DebugService:
    def __init__(self, base_url):
        self.base_url = base_url

    def recreate_database(self):
        endpoint = f"{self.base_url}/debug/recreate-database"
        headers = {
            "Accept": "*/*"
        }
        try:
            response = requests.post(endpoint, headers=headers)
            if response.status_code == 200:
                print("Baza danych została pomyślnie odtworzona.")
                return response.json() if response.content else {"message": "Recreate successful"}
            else:
                print(f"Błąd podczas odtwarzania bazy danych: {response.status_code}")
                response.raise_for_status()
        except requests.RequestException as e:
            print(f"Wystąpił błąd połączenia: {e}")
            raise

if __name__ == "__main__":
    # Konfiguracja adresu backendu
    base_url = "http://172.21.40.127:12038"
    service = DebugService(base_url)

    # Wywołanie końcówki
    try:
        result = service.recreate_database()
        print("Odpowiedź serwera:", result)
    except Exception as e:
        print("Nie udało się wywołać końcówki:", e)
