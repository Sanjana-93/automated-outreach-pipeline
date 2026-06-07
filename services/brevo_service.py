import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BREVO_API_KEY")


def send_email(to_email, name):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": API_KEY,
        "content-type": "application/json"
    }

    payload = {

        "sender": {
            "name": "Sanjana",
            "email": "sanju931981@gmail.com"
        },

        "to": [
            {
                "email": to_email,
                "name": name
            }
        ],

        "subject": "Test Email From Automated Outreach Pipeline",

        "htmlContent": f"""
        <html>
        <body>

        <h2>Hello {name}</h2>

        <p>
        This email was sent automatically from my outreach pipeline project.
        </p>

        </body>
        </html>
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)
    print(response.text)