import os 
import json
import shutil
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

current_directory = os.path.dirname(os.path.realpath(__file__))
config_file_path = os.path.join(current_directory, "config.json")

#Check for config file, create copy from template if none is found
check_config_file = os.path.isfile(config_file_path)

if not check_config_file:
    print('Could not find config file, creating one from template.')
    shutil.copyfile(current_directory + '/config_template.json', config_file_path)

with open(config_file_path) as config_file:
    config = json.load(config_file)


#Basic api post request, modify according to your needs 
def report_score_to_api(score):
    if len(config['score_report']['url']) != 0:
        report_score_url = config['score_report']['url']
        print('Sending schufa score to API: ' + report_score_url)
        data = { "score": score } 
        if len(config['score_report']['authorization']) != 0:
            headers = { "Authorization": 'Bearer ' + config['score_report']['authorization'] }
        else:
            headers = {}
        r = requests.post(report_score_url, timeout = 30, json = data, headers = headers)


# Let chrome run in detached headless mode if required, no visible window, depending on OS
chrome_options = Options()
if config['chrome_options']['headless']:
    chrome_options.add_argument("headless")
if config['chrome_options']['detached']:
    chrome_options.add_experimental_option("detach", True)

#Prevent chrome from aborting when run as root
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

#Navigate to meineschufa.de my account page
driver.get("https://www.meineschufa.de/de/my-account")
driver.implicitly_wait(10)

#Wait for cookie banner to load and accept all cookies, execute_script because of shadow root
time.sleep(3)
driver.execute_script("""return document.querySelector("#usercentrics-root").shadowRoot.querySelector('button[data-testid="uc-accept-all-button"]')""").click()

#Login into schufa account using credentials, then navigate to "Daten-Einblick" area
username = driver.find_element(by=By.ID, value="username")
password = driver.find_element(by=By.ID, value="password")
login_button = driver.find_element(by=By.ID, value="kc-login")

username.send_keys(config['schufa']['username'])
password.send_keys(config['schufa']['password'])
login_button.click()

time.sleep(3)

score_view_button = driver.find_element(by=By.ID, value="daten-einblick")
score_view_button.click()

time.sleep(1)

#Request 2fa sms token and fetch it from mitm-api
send_sms_button = driver.find_element(by=By.ID, value="sendSms")
send_sms_button.click()

time.sleep(15)

if len(config['2fa_api']['authorization']) != 0:
    headers = { "Authorization": 'Bearer ' + config['2fa_api']['authorization'] }
else:
    headers = {}
pin_request = requests.get(config['2fa_api']['url'], timeout = 30, headers = headers)

if pin_request.status_code != 200:
    print('Error: Could not fetch schufa 2fa token, aborting...')
    driver.quit()
    exit(2)

pin_request_response = pin_request.text

#Enter 2fa sms token and confirm, extract score from overview afterwards
sms_tan_input = driver.find_element(by=By.ID, value="sms-tan")
sms_tan_input.send_keys(pin_request_response)

sms_tan_confirm_button = driver.find_element(by=By.ID, value="kc-login")
sms_tan_confirm_button.click()

time.sleep(3)

score = driver.find_element(by=By.XPATH, value="//score-element")
score = score.get_attribute('score')

print('Schufa score: ' + score + '%')

#Store the score locally, pass it to an api, or do whatever you want with it, your decision
report_score_to_api(score)

driver.quit()