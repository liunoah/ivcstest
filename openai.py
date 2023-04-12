import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def mian():
    cmd2 = "start C:/Users/root/Desktop/debug"
    os.popen(cmd2)
    sleep(3)
    # chrome config
    ch_option = webdriver.ChromeOptions()
    ch_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # prefs = {
    #     # chrome不弹出的“是否接受xxx通知”
    #     'profile.default_content_setting_values.notifications': 2}
    # ch_option.add_experimental_option('prefs', prefs)
    # # chrome不显示是收到自动软件控制
    # ch_option.add_experimental_option('excludeSwitches', ['enable-automation'])
    #
    # # 忽略证书错误，不需要手动点高级选项
    # ch_option.add_argument('--ignore-certificate-errors')
    # 获取手机模式
    # mobile_emulation = {"deviceName": "iPhone 6"}
    # ch_option.add_experimental_option("mobileEmulation", mobile_emulation)
    # 同时开启麦克风和摄像头--重点 (自动允许获取摄像头和麦克风)
    # ch_option.add_argument('--use-fake-ui-for-media-stream')
    # ch_option.add_argument('--use-fake-device-for-media-stream')
    # if is_headless:
    # ch_option.add_argument('--headless')
    # ch_option.add_argument('--disable-cpu')

    # driver1 = webdriver.Chrome(options=ch_option)

    # 禁用chrome 展示为机器人
    # ch_option.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=ch_option)

    driver.get("https://baidu.com")
    # driver.get("https://chat.openai.com/chat")
    # driver.refresh()
    sleep(30)
    driver.find_element(By.TAG_NAME("textarea")).send_keys("ABCD")

    driver.quit()
    # driver_agent1 = webdriver.Chrome(options=ch_option)
    sleep(10)


    sleep(100)
    print(driver.current_url)

    driver.close()


mian()
