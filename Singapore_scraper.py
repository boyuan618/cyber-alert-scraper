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


def Singapore():
    """
        Function to get new SingCERT alerts
    """
    # Initialize the Chrome driver with the specified options
    service = Service(executable_path='./chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=options)

    # Your code here to interact with the page
    driver.get("https://www.csa.gov.sg/alerts-advisories")

    #Retrieve all alerts
    raw_alerts = driver.find_elements(By.XPATH, "/html/body/div[2]/section/div[1]/div/div/div/div[3]/div[1]/div/a")

    #Extract alerts in format (Title, Date, Link)
    alerts = []   

    for raw_alert in raw_alerts:
        alert = {"title":"", "date":"", "link":""}
        
        alert["title"] = raw_alert.get_attribute("aria-label").replace(",", " ")
        alert["date"] = raw_alert.find_element(By.CLASS_NAME, "m-card-article__note").text
        alert["link"] = "https://www.csa.gov.sg/" + raw_alert.get_attribute("href")
        
        #Prevent duplicates
        if alert not in alerts:
            alerts.append(alert)

    
    #Check if alert exists
    new_alerts = []
    with open("singapore.txt", "r+") as file:
        current_alert_titles = [line.split(",")[0] for line in file.readlines()]

        for alert in alerts:
            #If this is a new alert, write to file and also return alert
            if alert["title"] not in current_alert_titles:
                new_alerts.append(alert)
                file.write(f"{alert["title"]},{alert["date"]},{alert["link"]}\n")
           
    # It's a good practice to close the driver when you're finished
    driver.quit()
    
    return new_alerts

