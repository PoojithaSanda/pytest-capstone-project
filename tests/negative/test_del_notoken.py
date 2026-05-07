import requests

def test_delete_note_without_token():
    base_url = "https://practice.expandtesting.com/notes/api"

    # fake note id
    note_id = "1234567890"

    # DELETE WITHOUT AUTH 
    response = requests.delete(f"{base_url}/notes/{note_id}")

    # VERIFY FAILURE 
    assert response.status_code in [401, 403]