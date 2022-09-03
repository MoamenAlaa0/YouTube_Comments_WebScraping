from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

def parsing(url):
    # Creating Chrome Driver session object
    option =  webdriver.ChromeOptions() 
    # The Headless mode is a feature which allows the execution of a full version of the Chrome Browser
    # It provides the ability to control Chrome via external programs
    # The headless mode can run on servers without the need for dedicated display or graphics
    option.add_argument("--headless")
    # Open Chrome Driver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=option)
    # Get request to the webpage
    driver.get(url)
    
    # Returns height of the scroll in pixels
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, " + str(last_height) + ");")
        # Delay one second
        time.sleep(1)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        
        if new_height == last_height:
            break
        last_height = new_height
    
    # Parsing the html file
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # Quit from all the browser windows and terminates the WebDriver session
    driver.quit()

    # title = soup.select_one('#container > h1').text
    
    # Scraping the comments
    comments = soup.select("#content > #content-text")
    comment_list = [comment.text for comment in comments]
    return comment_list

def saving_csv(comment_list, file_name):
    data = pd.DataFrame({'comments': comment_list})
    data.to_csv(file_name, index = False)

url = 'https://www.youtube.com/watch?v=w8yWXqWQYmU'

list = parsing(url)
saving_csv(list, 'YouTube_WebScraping.csv')