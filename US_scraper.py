#Chrome version 131

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Configure Chrome options
options = webdriver.ChromeOptions()
options.headless = True  # Enable headless mode
options.add_argument("--window-size=1920,1200")  # Set the window size

# Set the path to the Chromedriver
DRIVER_PATH = '/chromedriver.exe'


def USA():
    """
        Function to get new US alerts
    """
    # Initialize the Chrome driver with the specified options
    service = Service(executable_path='./chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=options)

    # Your code here to interact with the page
    driver.get("https://www.cisa.gov/news-events/cybersecurity-advisories")

    #Retrieve all alerts
    raw_alerts = driver.find_elements(By.XPATH, "//div[@class='c-teaser__content']")

    #Extract alerts in format (Rating, Title, Date, Link)
    alerts = []   

    for raw_alert in raw_alerts:
        alert = {"rating":"", "title":"", "date":"", "link":""}
        
        alert["rating"] = raw_alert.find_element(By.CLASS_NAME, "c-teaser__meta").text
        alert["title"] = raw_alert.find_element(By.TAG_NAME, "span").text.replace(",", " ")
        alert["date"] = raw_alert.find_element(By.TAG_NAME, "time").text
        alert["link"] = "https://www.cisa.gov/" + raw_alert.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        #Prevent duplicates
        if alert not in alerts:
            alerts.append(alert)

    
    #Check if alert exists
    new_alerts = []
    with open("usa.txt", "r+") as file:
        current_alert_titles = [line.split(",")[1] for line in file.readlines()]

        for alert in alerts:
            #If this is a new alert, write to file and also return alert
            if alert["title"] not in current_alert_titles:
                new_alerts.append(alert)
                file.write(f"{alert["rating"]},{alert["title"]},{alert["date"]},{alert["link"]}\n")
           
    # It's a good practice to close the driver when you're finished
    driver.quit()
    
    return new_alerts

