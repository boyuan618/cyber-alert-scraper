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


def Japan_Vuln():
    """
        Function to get new JapanCert vulns
    """
    # Initialize the Chrome driver with the specified options
    service = Service(executable_path='./chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=options)

    # Your code here to interact with the page
    driver.get("https://jvn.jp/en/")

    #Retrieve all alerts
    news_list = driver.find_element(By.ID, "news-list")

    #Extract alerts in format (ID, Title, Date, Link)
    alerts = []
    
    
    raw_alerts = news_list.find_elements(By.TAG_NAME, "dl")
 
    for raw_alert in raw_alerts:
        alert = {"id":"", "title":"", "date":"", "link":""}

        #Parse text data
        text_data = raw_alert.text.split("\n")
        #Find where date starts
        date_index = text_data[1].index("[")
        
        alert["id"] = text_data[0].strip(":")
        alert["title"] = text_data[1][:date_index].strip().replace(",", " ")
        alert["date"] = text_data[1][date_index:].strip()
        alert["link"] = raw_alert.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        #Prevent duplicates
        if alert not in alerts:
            alerts.append(alert)


    #Check if alert exists
    new_alerts = []
    with open("japan vuln.txt", "r+") as file:
        current_alert_ids = [line.split(",")[0] for line in file.readlines()]

        for alert in alerts:
            #If this is a new alert, write to file and also return alert
            if alert["id"] not in current_alert_ids:
                new_alerts.append(alert)
                file.write(f"{alert["id"]},{alert["title"]},{alert["date"]},{alert["link"]}\n")
              
    # It's a good practice to close the driver when you're finished
    driver.quit()
    
    return new_alerts
