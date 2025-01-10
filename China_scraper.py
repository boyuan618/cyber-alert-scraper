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


def China():
    """
        Function to get new China alerts
    """
    # Initialize the Chrome driver with the specified options
    service = Service(executable_path='./chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=options)

    # Your code here to interact with the page
    driver.get("https://www.cert.org.cn/publish/english/115/index.html")

    #Retrieve all alerts
    #alert_table = driver.find_element(By.CLASS_NAME, "content")

    #Extract alerts in format (Title, Date, Link)
    alerts = []
   
    raw_alerts = driver.find_elements(By.XPATH, "//div[@class='content']/div[not(@class)]")

    for raw_alert in raw_alerts:
        alert = {"title":"", "date":"", "link":""}
    
        #Parse text data
        text_data = raw_alert.text
        
        #Find where date ends
        date_index = text_data.rfind("\n") #Date ends at last space
        
        
        alert["title"] = text_data[:date_index].strip()
        alert["date"] = text_data[date_index:].strip()
        alert["link"] = raw_alert.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        alerts.append(alert)


    #Check if alert exists
    new_alerts = []
    with open("china.txt", "r+") as file:
        current_alert_titles = [line.split(",")[0] for line in file.readlines()]

        for alert in alerts:
            #If this is a new alert, write to file and also return alert
            if alert["title"] not in current_alert_titles:
                new_alerts.append(alert)
                file.write(f"{alert["title"]},{alert["date"]},{alert["link"]}\n")
           
    # It's a good practice to close the driver when you're finished
    driver.quit()
    
    return new_alerts

China()