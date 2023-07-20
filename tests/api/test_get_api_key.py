from api import get_api_key


def test_get_api_key():
    assert get_api_key("tests/api/test_key.txt") == "ABC123"
