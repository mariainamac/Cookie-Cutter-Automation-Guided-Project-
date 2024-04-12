#importing files/libraries etc.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Helps to call the elements in the website CLASS,ID etc. to pull up the website
from selenium.webdriver.common.by import By

#Helps to click on the 'keyboard' eg. clicking 'ENTER' from a keyboard
from selenium.webdriver.common.keys import Keys

#Helps to wait until the 'element' appears ie if you have slow internet etc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Chrome webdriver file execution
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#The link on which website we want to go
driver.get("https://www.google.com")

#Using the 'wait' library to wait for an element to appear (due to slow internet)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

#Helps to call the elements in the website CLASS,ID etc. to pull up the website
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
#Helps to click on the 'keyboard' eg. clicking 'ENTER' from a keyboard
input_element.send_keys("cookie clicker" + Keys.ENTER)

#Using the 'wait' library to wait for an element to appear (due to slow internet)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Cookie Clicker - Orteil"))
)

#Helps to find the name of the link that you input and click on it
link=driver.find_element(By.PARTIAL_LINK_TEXT, "Cookie Clicker - Orteil")
link.click()

#https://orteil.dashnet.org/cookieclicker/

cookie_id = "bigCookie"
cookies_id = "cookies"
product_prefix = "product"
product_price_prefix = "productPrice"

#Using the 'wait' library to wait for an element to appear (due to slow internet)
#'.XPATH' helps to precisely locate elements inside HTML or XML document or website
#Below .XPATH helps to locate a text 'English' inside the HTML or XML website
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

#Helps to find the name of the link that you input and click on it
language=driver.find_element(By.XPATH,"//*[contains(text(), 'English')]")
language.click()

#Using the 'wait' library to wait for an element to appear (due to slow internet)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

#Helps to find the name of the link that you input and click on it
cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

#Helps to continuously click the cookie again and again in a loop
while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

#Helps to extract out the product price and then converting it to integer for further query
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

#Helps to purchase the product in the game web once cookie count is enough to purchase
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break