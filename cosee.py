import _thread
import csv
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# no care https waning
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
is_headless = 0
url = "https://192.168.10.31:3004/test.html"
response = requests.get('https://192.168.10.31:3004/rooms/', verify=False)
response = response.json()


def agent():
    # chrome config
    ch_option = webdriver.ChromeOptions()
    prefs = {
        # chrome不弹出的“是否接受xxx通知”
        'profile.default_content_setting_values.notifications': 2}
    ch_option.add_experimental_option('prefs', prefs)
    # chrome不显示是收到自动软件控制
    ch_option.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 忽略证书错误，不需要手动点高级选项
    ch_option.add_argument('--ignore-certificate-errors')
    # 获取手机模式
    # mobile_emulation = {"deviceName": "iPhone 6"}
    # ch_option.add_experimental_option("mobileEmulation", mobile_emulation)
    # 同时开启麦克风和摄像头--重点 (自动允许获取摄像头和麦克风)
    ch_option.add_argument('--use-fake-ui-for-media-stream')
    ch_option.add_argument('--use-fake-device-for-media-stream')
    if is_headless:
        ch_option.add_argument('--headless')
        ch_option.add_argument('--disable-cpu')

    # driver1 = webdriver.Chrome(options=ch_option)
    driver_agent = webdriver.Chrome(options=ch_option)
    # driver_agent1 = webdriver.Chrome(options=ch_option)

    driver_agent.get("file:///C:/")
    for index in range(0, 10):
        sleep(1)
        print('window.open("' + url + '?room=' + response[index]['id'] + '");')
        for j in range(0, 1):
            sleep(1)
            js = 'window.open("' + url + '?room=' + response[index]['id'] + '");'
            driver_agent.execute_script(js)



for index1 in range(0, 1):
    _thread.start_new_thread(agent, ())
sleep(60000)
