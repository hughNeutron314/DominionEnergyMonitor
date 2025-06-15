import os
from dotenv import load_dotenv

required_vars = [
    "DOMINION_USERNAME", "DOMINION_PASSWORD", "DOMINION_LOGIN_URL", 
    "DOMINION_API_URL", "DOMINION_ACCOUNT_NUMBER", "DOMINION_ACTION_CODE",
    "DOMINION_LONG_LIVED_TOKEN", "MQTT_HOST", "MQTT_PORT", "MQTT_USERNAME", "MQTT_PASSWORD"
]

load_dotenv()

for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"Missing required env var: {var}")

DOMINION_USERNAME = os.getenv("DOMINION_USERNAME")
DOMINION_PASSWORD = os.getenv("DOMINION_PASSWORD")
DOMINION_LOGIN_URL = os.getenv("DOMINION_LOGIN_URL")
DOMINION_ACCOUNT_NUMBER = os.getenv("DOMINION_ACCOUNT_NUMBER")
DOMINION_ACTION_CODE = os.getenv("DOMINION_ACTION_CODE")
DOMINION_API_URL = os.getenv("DOMINION_API_URL")
DOMINION_LONG_LIVED_TOKEN = os.getenv("DOMINION_LONG_LIVED_TOKEN")

MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")        