import os
from dotenv import load_dotenv

load_dotenv()

def get_variable_value(var_key:str):
    return os.getenv(var_key)

def get_all_variables():
    return os.environ.items()

if __name__ == "__main__":

    def print_all_env_variables():
        print("All variables:")
        for key, value in get_all_variables():
            print(f"{key}: {value}")

    print_all_env_variables()