import logging
from Dominion.dominion_api import DominionApi
from Dominion.token_generator import TokenGenerator
from HomeAssistant.mqtt_publisher import MqttPublisher
from config import DOMINION_LONG_LIVED_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/dominion_scraper.log"),
        logging.StreamHandler()
    ]
)

logging.info("Starting..")

tokenGenerator = TokenGenerator()
dominionApi = DominionApi()
mqttPublisher = MqttPublisher()

try:
    token = DOMINION_LONG_LIVED_TOKEN or tokenGenerator.get_bearer_token()

    if not token:
        logging.critical("Unable to get a valid token exiting")
        exit(1)

    usage = dominionApi.get_current_usage(token)

    logging.info(f"\n\n === USAGE : {usage} kWh ===")

    mqttPublisher.publish_discovery_config()
    mqttPublisher.publish_usage(usage)
except Exception as e:
    logging.error(e)
    mqttPublisher.close()