import requests
BASE_URL = "https://practice.expandtesting.com/notes/api"


def test_delete_note_with_invalid_token():

    # INVALID TOKEN
    invalid_token = "invalid_token_123"

    headers = {
        "x-auth-token": invalid_token
    }

    # RANDOM INVALID NOTE ID
    note_id = "123456"

    # SEND DELETE REQUEST
    response = requests.delete(
        f"{BASE_URL}/notes/{note_id}",
        headers=headers
    )

    # PRINT RESPONSE
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    # VERIFY DELETE FAILED
    assert response.status_code == 401

    # VERIFY ERROR MESSAGE
    response_text = response.text.lower()

    assert (
        "not valid" in response_text
        or
        "expired" in response_text
        or
        "login" in response_text
        or
        "token" in response_text
    )

    print("Invalid token cannot delete note")