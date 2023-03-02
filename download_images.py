# Import the packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from dotenv import load_dotenv
import os
import time
from datetime import datetime
from pathlib import Path
import shutil
from joblib import Parallel, delayed

# Load environment variables
load_dotenv()

# Define global inputs from the .env file
url = os.getenv(key="url")
start_date = os.getenv(key="start_date")
end_date = os.getenv(key="end_date")
user_name = os.getenv(key="user_name")
password = os.getenv(key="password")

# Set the Chrome options
chrome_options = Options()
chrome_options.add_argument("start-maximized") # Required for a maximized Viewport
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation', 'disable-popup-blocking']) # Disable pop-ups to speed up browsing
chrome_options.add_experimental_option("detach", True) # Keeps the Chrome window open after all the Selenium commands/operations are performed 
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'}) # Operate Chrome using English as the main language
chrome_options.add_argument('--blink-settings=imagesEnabled=false') # Disable images
chrome_options.add_argument('--disable-extensions') # Disable extensions
chrome_options.add_argument("--headless=new") # Operate Selenium in headless mode
chrome_options.add_argument('--no-sandbox') # Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only
chrome_options.add_argument('--disable-gpu') # An additional Selenium setting for headless to work properly, although for newer Selenium versions, it's not needed anymore
chrome_options.add_argument("--window-size=1920x1080") # Set the Chrome window size to 1920 x 1080

# Generate a sequence of dates that will define the file names to download
dates = pd.date_range(start=start_date, end=end_date, freq="1D").strftime("%Y%m%d").tolist()

def download_func(date):
    # Set the file name
    file_name = f"SVDNB_npp_d{date}.rade9d.tif"

    # Instantiate a webdriver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    print(f"[{file_name} status] - Navigating to the URL https://eogdata.mines.edu/nighttime_light/nightly/rade9d/?C=N;O=D to download the images")
    driver.get(url)

    # Maximize the window
    driver.maximize_window()

    # Navigate to the page corresponding to the date of the iteration
    print(f"[{file_name} status] - Finding the file name with the date {date} and clicking on it")
    driver.find_element(by=By.XPATH, value=f"//td[@class='indexcolname']/a[text()='{file_name}']").click()
    
    # Wait until the username field appears and then proceeed
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
    except TimeoutException:
        return

    # Click on the username field and insert the username
    print(f"[{file_name} status] - Inputting the username and password to download the file...")
    driver.find_element(by=By.XPATH, value="//input[@id='username']").send_keys(user_name)
    driver.find_element(by=By.XPATH, value="//input[@id='password']").send_keys(password)
    driver.find_element(by=By.XPATH, value="//input[@id='kc-login']").click()

    # Wait for 2 seconds for the download to start
    time.sleep(2)

    # Check if the file exists in the working directory
    path = Path(f"{os.getenv(key='downloads_dir')}/{file_name}")
    t1 = datetime.now()

    # If the file doesn't exist, print a message saying that we are still waiting for the file to appear and wait 30 seconds before proceeding to the next command
    while path.is_file() == False:
        t2 = datetime.now()
        print(f"[{file_name} status] - Still waiting for the {file_name} to download. {t2 - t1} have elapsed thus far")
        time.sleep(30)

        # If the file exists, print a success message, close the driver, and move the file from the Downloads folder to the current directory
        if path.is_file() == True:
            print(f"[{file_name} status] - The file {file_name} has been downloaded. Closing the driver now...")

            # Close the driver
            driver.quit()

            # Move the file from the downloads folder to the current directory
            shutil.move(src=f"{os.getenv(key='downloads_dir')}/{file_name}", dst=f"{os.getcwd()}/{file_name}")
            print(f"[{file_name} status] - Moved the file {file_name} to the current working directory. Moving to the next date...\n")
            
            # Break out of the loop
            break

# Run the function in parallel
Parallel(n_jobs=int(os.getenv("pages_to_download_at_once")), verbose=13)(delayed(download_func)(date=date) for date in dates)

# print a success message that the program finished running
print("Finished downloading all the tiff files. Terminating the program...")