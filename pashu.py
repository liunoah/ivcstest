import _thread
import csv
import os

import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# no care https waning
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
is_headless = 0
url = "http://www.biqigewx.com/146_146138/48985553.html"


def agent():
    if os.path.exists("3.txt"):
        os.remove("3.txt")

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
    # ch_option.add_argument('--use-fake-ui-for-media-stream')
    # ch_option.add_argument('--use-fake-device-for-media-stream')
    # if is_headless:
    ch_option.add_argument('--headless')
    ch_option.add_argument('--disable-cpu')

    # driver1 = webdriver.Chrome(options=ch_option)
    driver_agent = webdriver.Chrome(options=ch_option)
    # driver_agent1 = webdriver.Chrome(options=ch_option)
    start_url = "http://www.kuaishu8.com/zhongshengzhiqinshihuangchangzizhaolang/28577759.html"
    end_url = "http://www.kuaishu8.com/zhongshengzhiqinshihuangchangzizhaolang/28577770.html"

    driver_agent.get(start_url)

    print(driver_agent.current_url)
    while driver_agent.current_url != end_url:
        print(driver_agent.current_url)
        content = driver_agent.find_element(By.ID, "htmlContent")
        book_title = driver_agent.find_elements(By.CLASS_NAME, "readTitle")[0]
        print(book_title.text)
        print(content.text)
        # if len(book_title) == 2:
        #     bookName = "第" + book_title[1]
        #     print(bookName)
        # else:
        #     bookName = "第" + book_title[0]
        #     print(bookName)
        with open("3.txt", "a+", encoding='utf-8') as f:
            f.write("\n" + str(book_title.text) + "\n")
            f.write(content.text)
            f.close()
        driver_agent.find_element(By.ID, "linkNext").click()

    sleep(5)
    driver_agent.get("http://www.biqigewx.com/146_146138/48985555.html")
    js = 'window.open("+' + url + '");'
    driver_agent.execute_script(js)
    sleep(10)
    driver_agent.close()


agent()
