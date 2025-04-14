import json, logging
import paho.mqtt.client as mqtt
from config import MQTT_HOST, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD

class MqttPublisher:
    def __init__(self):
        self.client = mqtt.Client()

        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.connect(MQTT_HOST, MQTT_PORT, 60)

    def publish_discovery_config(self):
        logging.info("Publishing discovery config")

        topic = "homeassistant/sensor/dominion_energy/config"
        payload = {
            "name": "Dominion Energy Usage",
            "unique_id": "dominion_energy_usage_sensor",
            "state_topic": "homeassistant/sensor/dominion_energy/state",
            "unit_of_measurement": "kWh",
            "device_class": "energy",
            "state_class": "total",
            "icon": "mdi:flash",
            "availability_topic": "homeassistant/sensor/dominion_energy/availability"
        }
        result = self.client.publish(topic, json.dumps(payload), retain=True)
        logging.debug(f"Config Result: {result.rc}")

    def publish_usage(self, usage_value):
        logging.info(f"Publishing Usage: {usage_value}")

        result = self.client.publish("homeassistant/sensor/dominion_energy/state", str(usage_value), retain=True)
        logging.debug(f"Data Result: {result.rc}")

        result = self.client.publish("homeassistant/sensor/dominion_energy/availability", "online", retain=True)
        logging.info(f"Status Result: {result.rc}")

    def close(self):
        logging.info("Closing..")

        self.client.publish("homeassistant/sensor/dominion_energy/availability", "offline", retain=True)
        self.client.disconnect()