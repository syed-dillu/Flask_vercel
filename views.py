import time
from flask import Blueprint, render_template, request, jsonify,redirect, url_for
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# load_dotenv()
# host = os.getenv("HOST")
# port = os.getenv("PORT")

views = Blueprint(__name__, "views")

@views.route("/")
def index():
    return render_template('index.html',)


@views.route("/hello")
def hell():
    return render_template('hello')

@views.route("/param_users/<username>")
def user_param(username):
    return render_template('index.html', name = username)

   
@views.route("/query_users")
def user_query():
    args = request.args
    username = args.get('name')
    return render_template('index.html', name = username)

@views.route("/json")
def get_json():
    return jsonify ({
        "name" : "tom",
        "age": 34
    })

@views.route("/hello")
def get_hell():
    return "Hello how are u"

@views.route('/signup', methods=['GET', 'POST'])
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


@views.route("go_to_home")
def return_home():
    return redirect(url_for("views.get_json"))

    