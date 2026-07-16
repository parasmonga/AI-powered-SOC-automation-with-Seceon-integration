import requests
import urllib3

from config.seceon_config import (
    SECEON_BASE_URL,
    TENANT_ID,
    BEARER_TOKEN,
    VERIFY_SSL,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SeceonClient:

    def __init__(self):

        # Create HTTP Session
        self.session = requests.Session()

        # Default Headers
        self.session.headers.update({

            "Authorization": f"Bearer {BEARER_TOKEN}",

            "Accept": "application/json, text/plain, */*",

            "Content-Type": "application/json",

            "tenant_id": TENANT_ID,

            "locale": "en-US",

            "timezone": "Asia/Calcutta",

            "Origin": SECEON_BASE_URL,

            "Referer": f"{SECEON_BASE_URL}/nextgen/v1/",

            "User-Agent": "Mozilla/5.0"

        })

    def fetch_alerts(self):

        url = (
            f"{SECEON_BASE_URL}"
            "/uiserver/v1/read/tenant/new-alert-analysis/fetch"
        )

        payload = {

            "tenant_id": TENANT_ID,

            "from": "7d",

            "to": "now",

            "time_range_type": "commonly used",

            "severity": "",

            "status": "",

            "assigned": "",

            "uda": ""

        }

        response = self.session.post(

            url,

            json=payload,

            verify=VERIFY_SSL,

            timeout=30

        )

        print("Status Code :", response.status_code)
        print("Response Body :")
        print(response.text)

        response.raise_for_status()

        return response.json()