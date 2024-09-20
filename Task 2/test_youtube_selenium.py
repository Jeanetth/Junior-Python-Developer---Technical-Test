from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Import webdriver manager
import time

# Configure Chrome driver with webdriver-manager
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open the window maximized

# Use webdriver-manager to download and configure ChromeDriver automatically
service = Service(ChromeDriverManager().install())

# Initialize the browser with the automatically downloaded ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the specific YouTube video
    driver.get("https://www.youtube.com/watch?v=mifElrSN0SQ&t")

    # Wait for the video to load
    time.sleep(5)

    # Subscribe to the channel (make sure you're logged in)
    try:
        subscribe_button = driver.find_element(By.XPATH, '//ytd-subscribe-button-renderer//yt-formatted-string[text()="Subscribe"]')
        subscribe_button.click()
        time.sleep(2)  # Wait for the action to complete
    except:
        print("Already subscribed or could not find the Subscribe button")

    # Like the video (make sure you're logged in)
    try:
        like_button = driver.find_element(By.XPATH, '//ytd-toggle-button-renderer[@is-icon-button]/a[@aria-label="Like this video"]')
        like_button.click()
        time.sleep(2)  # Wait for the action to complete
    except:
        print("Already liked or could not find the Like button")

    # Wait a few seconds to confirm actions before closing
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
