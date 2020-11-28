# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Mailjet
from mailjet_rest import Client

# Constants / Secrets
from config import config, secret


# Set Firefox to Headless
options = webdriver.FirefoxOptions()
options.headless=True

# Create Driver Instance
driver = webdriver.Firefox(options=options)

# Get Link
driver.get(LINK)

# Find Button for 1.16
button = driver.find_element_by_name(BUTTON1_ELEMENT)
user_input = driver.find_element_by_id(INPUT1_ELEMENT)
ActionChains(driver).move_to_element(button).click(user_input).perform()

# Find RSG Button
button = driver.find_element_by_name(BUTTON2_ELEMENT)
user_input = driver.find_element_by_id(INPUT2_ELEMENT)
ActionChains(driver).move_to_element(button).click(user_input).perform()

# Wait for Page Load
driver.implicitly_wait(3)

# Finds All Speedrunners
content = driver.find_elements_by_css_selector(NAME_CSS_SELECTOR)

# Print Speedrunners
for item in content:
    if (item.text) == USERNAME:
        message = "Elysaku Pog"
        mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='v3.1')
        data = {
        'Messages': [{"From": {"Email": SENDER_EMAIL,"Name": SENDER_NAME},
                    "To": [{"Email": RECIEVER_EMAIL,"Name": RECIEVER_NAME}
                            ],
                    "Subject": "Kara Tutoring Email Credentials",
                    "TextPart": message
                    }
            ]
        }
        mailjet.send.create(data=data)

# Close Browser
driver.close()
