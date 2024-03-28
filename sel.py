import time
from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the signup page'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    driver = webdriver.Chrome()

    driver.get('https://stgapp.tutelar.io/signin')
    email_id = driver.find_element(By.NAME,"email")
    email_id.send_keys("wewekoj430@fashlend.com")


    pass_i = driver.find_element(By.NAME, "password")
    pass_i.send_keys("Test@123")

    check_box = driver.find_element(By.ID, "terms-section")
    check_box.click()
    time.sleep(2)

    button = driver.find_element(By.XPATH, "//span[text()='LOGIN']")
    button.click()

    return 'Signup successful'

if __name__ == '__main__':
    app.run(debug=True)
