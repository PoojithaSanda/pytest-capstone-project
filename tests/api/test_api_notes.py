from api.api_client import APIClient

def test_get_notes():
    api = APIClient("https://practice.expandtesting.com/notes/api")
    api.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")
    res = api.get_notes()

    assert res.status_code == 200
    assert isinstance(res.json()["data"], list)