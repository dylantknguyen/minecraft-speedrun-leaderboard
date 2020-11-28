# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Mailjet
from mailjet_rest import Client

# Logging
from logging import basicConfig, info, INFO

# Constants / Secrets
from config import config, secret

# Basic Logging Config
basicConfig(filename ='app.log', level = INFO)

# Set Firefox to Headless
options = webdriver.FirefoxOptions()
options.headless=True

# Create Driver Instance
driver = webdriver.Firefox(options=options)
info("Opening Firefox Headless")

# Get Link
driver.get(config.LINK)
info("Opening Link")

# Find Button for 1.16
button = driver.find_element_by_name(config.BUTTON1_ELEMENT)
user_input = driver.find_element_by_id(config.INPUT1_ELEMENT)
ActionChains(driver).move_to_element(button).click(user_input).perform()
info("Clicking 1.16 Button")

# Find RSG Button
button = driver.find_element_by_name(config.BUTTON2_ELEMENT)
user_input = driver.find_element_by_id(config.INPUT2_ELEMENT)
ActionChains(driver).move_to_element(button).click(user_input).perform()
info("Clicking RSG Button")

# Wait for Page Load
driver.implicitly_wait(3)

# Finds All Speedrunners
content = driver.find_elements_by_css_selector(config.NAME_CSS_SELECTOR)
info("Finding All Speedrunners")


# Print Speedrunners
for item in content:
    info(f"Speedrunner: {item.text}")
    if (item.text) == config.USERNAME:
        message = "Elysaku Pog"
        mailjet = Client(auth=(secret.MAILJET_API_KEY, secret.MAILJET_API_SECRET), version='v3.1')
        data = {
        'Messages': [{"From": {"Email": secret.SENDER_EMAIL,"Name": secret.SENDER_NAME},
                    "To": [{"Email": secret.RECIEVER_EMAIL,"Name": secret.RECIEVER_NAME}
                            ],
                    "Subject": "Kara Tutoring Email Credentials",
                    "TextPart": message
                    }
            ]
        }
        mailjet.send.create(data=data)

# Close Browser
driver.close()
