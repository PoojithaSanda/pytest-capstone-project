import requests
BASE_URL = "https://practice.expandtesting.com/notes/api"

def test_delete_note_with_invalid_token():

    invalid_token = "invalid_token_123"

    headers = {
        "x-auth-token": invalid_token
    }

    note_id = "123456"

    response = requests.delete(
        f"{BASE_URL}/notes/{note_id}",
        headers=headers
    )

    # PRINT RESPONSE FOR DEBUGGING
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    # VERIFY UNAUTHORIZED ACCESS
    assert response.status_code == 401