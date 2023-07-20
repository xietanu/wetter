API_KEY_FILEPATH = "api_key.txt"


def get_api_key(filepath: str = API_KEY_FILEPATH) -> str:
    """Reads the API key from a text file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        api_key = file.read()
    return api_key


API_KEY = get_api_key(API_KEY_FILEPATH)
