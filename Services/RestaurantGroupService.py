class RestaurantGroupService:
    def __init__(self, api_service):
        self.api_service = api_service

    def get_restaurants_groups(self):
        response = self.api_service.get('my-restaurant-groups')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch restaurants groups, status code: {response.status_code}"}