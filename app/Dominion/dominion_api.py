import requests, logging
from config import DOMINION_ACTION_CODE, DOMINION_ACCOUNT_NUMBER, DOMINION_API_URL

class DominionApi:
    
    def get_headers(self, token):
        return {
            "Authorization": f"{token}",
            "uid": "1",
            "pt": "1",
            "channel": "WEB",
            "Origin": "https://myaccount.dominionenergy.com",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
        }

    def get_params(self):
        return {
            "accountNumber": DOMINION_ACCOUNT_NUMBER,
            "actionCode": DOMINION_ACTION_CODE
        }

    def get_current_usage(self, token) -> str:
        logging.info(f"Using Token: {token}")

        headers = self.get_headers(token)
        params = self.get_params()

        response = requests.get(DOMINION_API_URL, headers=headers, params=params)
        data = response.json()

        logging.info(f"Data: {data}\n\n")

        status_code = int(data.get("status", {}).get("code"))
        status_msg = data.get("status", {}).get("message")

        logging.info(f"Status Code: {status_code}, Status Message: {status_msg}")

        if not status_code == 200: return "Unknown"

        current_usage = data.get("data", {}).get("currentUsageKwh")
        logging.info(f"Current usage this month: {current_usage} kWh")

        return current_usage