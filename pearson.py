from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from win10toast import ToastNotifier
toast = ToastNotifier()

driver = webdriver.Chrome()
driver.get("https://login.pearson.com/v1/piapi/piui/signin?client_id=dN4bOBG0sGO9c9HADrifwQeqma5vjREy&okurl=https:%2F%2Fmycourses.pearson.com%2Fcourse-home&siteid=8313")
user = driver.find_element(By.XPATH, "//div[@class='ah-full-username']/input")
user.send_keys("Username")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("password")

button = driver.find_elements(By.XPATH, "//div[@class='pe-form--group']")[3]
button.click()

time.sleep(7)

course = driver.find_element(By.XPATH, "//span[@class='title ellipsis card-font']")
course.click()

time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

completed = driver.find_elements(By.XPATH, "//div[@class='item-name']")[1]
#completed = completed.find_elements(By.XPATH, "//div/div/div/div")[2]
completed.click()

time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
activity = driver.find_element(By.XPATH,"//iframe[@id='contentFrame']")
driver.switch_to.frame(activity)
time.sleep(2)
for j in range(1, 20, 2):
    act = driver.find_elements(By.CSS_SELECTOR, 'a.row--div--link')[j]#/div[@id='content']/div/section/table")
    act.click()
    #time.sleep(2)
    #driver.refresh()
    time.sleep(3)
    #activity = driver.find_element(By.XPATH,"//iframe[@class='_3D-_ic2VpzuE6BaMkv2xcs']")
    #activity = driver.find_element(By.XPATH,"//iframe[@id='contentFrame']")
    #driver.switch_to.frame(activity)
    acts = driver.find_elements(By.XPATH, "//a[@class='btn btn-default btn-practice']")
    for i in range(0, len(acts)):#length):
        try:
            time.sleep(2)
            act = driver.find_elements(By.XPATH, "//a[@class='btn btn-default btn-practice']")[i]#/div[@id='content']/div/section/table")
            act.click()
            time.sleep(2)
            requests = driver.find_elements(By.XPATH, "//span[@class='answer-button request-answer enabled']")

            for r in requests:
                r.click()
                time.sleep(2)
                button = driver.find_element(By.XPATH, "//button[@class='yui3-button yui3-button-primary']")
                button.click()
                time.sleep(2)

            back = driver.find_element(By.XPATH, "//a[@class='return-assignment-link']")
            back.click()
            time.sleep(1)
        except:
            pass
    toast.show_toast(
        "Notification",
        "Notification body",
        duration = 20,
        icon_path = "icon.ico",
        threaded = True,
    )
    time.sleep(4)
    driver.switch_to.default_content()
    time.sleep(4)
    completed = driver.find_elements(By.XPATH, "//div[@class='item-name']")[1]
    #completed = completed.find_elements(By.XPATH, "//div/div/div/div")[2]
    completed.click()
    time.sleep(5)
    activity = driver.find_element(By.XPATH,"//iframe[@id='contentFrame']")
    driver.switch_to.frame(activity)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)
    
    
