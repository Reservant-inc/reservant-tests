import pickle
import os


class LocalBearerService:
    def __init__(self, token_file='bearer_token.pkl'):
        self.token_file = token_file

    def save_bearer_token(self, bearer_token):
        with open(self.token_file, 'wb') as f:
            pickle.dump(bearer_token, f)

    def get_bearer_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as f:
                return pickle.load(f)
        return ""
