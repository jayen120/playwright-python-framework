import os

ENV = os.getenv("ENV", "dev")

CONFIG = {
    "dev": {
        "BASE_URL": "https://www.saucedemo.com/"
    },
    "staging": {
        "BASE_URL": "https://www.saucedemo.com/"
    }
}

BASE_URL = CONFIG[ENV]["BASE_URL"]


USERNAME = "standard_user"
PASSWORD = "secret_sauce"