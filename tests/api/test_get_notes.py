def test_get_notes_api():
    from api.api_client import APIClient

    api = APIClient("https://practice.expandtesting.com/notes/api")

    # ---------------- LOGIN ----------------
    api.login("sandapoojitha7396@gmail.com", "Poojitha@2k4")

    # ---------------- GET NOTES ----------------
    response = api.get_notes()

    assert response.status_code == 200

    data = response.json().get("data", [])

    # Basic validation
    assert isinstance(data, list)

    # Optional: check at least one note exists
    assert len(data) >= 0