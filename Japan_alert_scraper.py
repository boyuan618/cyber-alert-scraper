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


def Japan_Alert():
    """
        Function to get new JapanCert alerts
    """
    # Initialize the Chrome driver with the specified options
    service = Service(executable_path='./chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=options)

    # Your code here to interact with the page
    driver.get("https://www.jpcert.or.jp/english/at/")

    #Retrieve all alerts
    news_list = driver.find_element(By.TAG_NAME, "tbody")

    #Extract alerts in format (Title, Date, Link)
    alerts = []
    
    raw_alerts = news_list.find_elements(By.TAG_NAME, "tr")[1:] #Remove first row which is heading
 
    for raw_alert in raw_alerts:
        alert = {"title":"", "date":"", "link":""}
    
        #Parse text data
        text_data = raw_alert.text
        
        #Find where date ends
        date_index = text_data.find(" ") #Date ends at first space
        
        #Find where title ends
        title_index = text_data.rfind(" ") #Title ends at last space
        
        alert["title"] = text_data[date_index:title_index].strip()
        alert["date"] = text_data[:date_index].strip()
        alert["link"] = raw_alert.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        alerts.append(alert)


    #Check if alert exists
    new_alerts = []
    with open("japan alert.txt", "r+") as file:
        current_alert_titles = [line.split(",")[0] for line in file.readlines()]

        for alert in alerts:
            #If this is a new alert, write to file and also return alert
            if alert["title"] not in current_alert_titles:
                new_alerts.append(alert)
                file.write(f"{alert["title"]},{alert["date"]},{alert["link"]}\n")
           
    # It's a good practice to close the driver when you're finished
    driver.quit()
    
    return new_alerts

Japan_Alert()