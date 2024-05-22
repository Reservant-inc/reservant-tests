class RestaurantService:
    def __init__(self, api_service):
        self.api_service = api_service

    def get_restaurants(self):
        response = self.api_service.get('my-restaurants')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch restaurants, status code: {response.status_code}"}
