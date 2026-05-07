
import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
    


    def login(self, email, password):
        res = requests.post(
            f"{self.base_url}/users/login",
            data={"email": email, "password": password}
        )

        print(res.json())  # DEBUG

        assert res.status_code == 200, "Login failed"

        self.token = res.json()["data"]["token"]

    def get_notes(self):
        return requests.get(
            f"{self.base_url}/notes",
            headers={"x-auth-token": self.token}
        )

    def delete_note(self, note_id):
        return requests.delete(
            f"{self.base_url}/notes/{note_id}",
            headers={"x-auth-token": self.token}
        )