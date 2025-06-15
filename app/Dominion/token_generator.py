from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, logging
from config import DOMINION_USERNAME, DOMINION_PASSWORD, DOMINION_LOGIN_URL, DOMINION_API_URL

class TokenGenerator:

    DOMINION_VALID_TKN_LENGTH = 583

    def get_bearer_token(self):
        logging.info(f"get_bearer_token - UserName: {DOMINION_USERNAME}")

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

        try:
            driver.get(DOMINION_LOGIN_URL)

            wait = WebDriverWait(driver, 15)
            email_field = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@placeholder, 'Email')]")
            ))

            email_field.send_keys(DOMINION_USERNAME)
            logging.info("Email entered")

            password_field = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[contains(@placeholder, 'Password')]")
            ))

            password_field.send_keys(DOMINION_PASSWORD)
            logging.info("Password entered")

            submit_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='submit' and @value='Submit']")
            ))

            submit_button.click()
            logging.info("Submit button clicked, sleeping for 10 seconds..")

            time.sleep(20)  # Wait for webpage to load and api requests to be made.
            
            for request in driver.requests:
                #token = request.headers["authorization"]
                #logging.critical(f"AUTH HEADER: {token}")

                if request.response and DOMINION_API_URL in request.url:
                    token = request.headers["authorization"]
                    logging.info(f"Valid token found with API: {token}\n\n")
                    return token

            logging.warning(f"No token found with API: {DOMINION_API_URL}, using alternative method to obtain token")

            for request in driver.requests:
                if "authorization" in request.headers:
                    token = request.headers["authorization"]
            
                    if len(token) == self.DOMINION_VALID_TKN_LENGTH:
                        print(f"Valid token found: {token}\n\n")
                        return token
            
            logging.error("No valid token found")
            return None
        finally:
            driver.quit()