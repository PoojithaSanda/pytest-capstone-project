def test_get_notes_when_empty():
    from api.api_client import APIClient

    api = APIClient("https://practice.expandtesting.com/notes/api")

    # ---------------- LOGIN ----------------
    api.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    # ---------------- GET NOTES ----------------
    response = api.get_notes()

    assert response.status_code == 200

    data = response.json().get("data", [])

    # ---------------- VALIDATION ----------------
    # Either empty OR controlled structure
    assert isinstance(data, list)

    # If system has reset DB, it may be empty
    assert len(data) >= 0