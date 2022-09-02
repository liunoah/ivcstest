import _thread
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://ivcs-test-k8s-azure.zealcomm.cn/"
time_interval = 2
is_headless = 0
user_num = 5
concurrent_interval = 3
start_user = 1



# 访客
def client():
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
    # # no load img
    # ch_option.add_argument('--blink-settings=imagesEnabled=false')
    # 获取手机模式
    mobile_emulation = {"deviceName": "iPhone 6"}
    ch_option.add_experimental_option("mobileEmulation", mobile_emulation)
    # 同时开启麦克风和摄像头--重点 (自动允许获取摄像头和麦克风)
    ch_option.add_argument('--use-fake-ui-for-media-stream')
    ch_option.add_argument('--use-fake-device-for-media-stream')
    if is_headless:
        ch_option.add_argument('--headless')
        ch_option.add_argument('--no-sandbox')
        ch_option.add_argument('--disable-dev-shm-usage')

    driver_agent = webdriver.Chrome(options=ch_option)
    # driver1 = webdriver.Chrome(options=ch_option)

    driver_agent.get(url + "customer/#/")

    windows = driver_agent.window_handles

    # input username and password login
    input_tag = driver_agent.find_elements(By.TAG_NAME, 'input')
    input_tag[0].send_keys("003")
    input_tag[1].send_keys("123456")
    input_tag[2].send_keys("noah")
    sleep(time_interval)
    driver_agent.find_element(By.CLASS_NAME, 'defaultbackColor').click()
    sleep(time_interval)
    driver_agent.find_elements(By.TAG_NAME, 'img')[1].click()
    sleep(time_interval)
    driver_agent.find_elements(By.TAG_NAME, 'span')[2].click()
    sleep(time_interval)
    driver_agent.find_elements(By.CLASS_NAME, 'ivu-dropdown-item')[0].click()
    sleep(time_interval)
    driver_agent.find_elements(By.CLASS_NAME, 'defaultbackColor')[0].click()

    sleep(1500)
    driver_agent.quit()


def agent(user, pw):
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
        ch_option.add_argument('--disable-gpu')

    driver_agent = webdriver.Chrome(options=ch_option)
    # driver1 = webdriver.Chrome(options=ch_option)

    driver_agent.get(url + "agent/#/")

    windows = driver_agent.window_handles

    # input username and password login
    input_tag = driver_agent.find_elements(By.TAG_NAME, 'input')
    input_tag[0].send_keys(user)
    input_tag[1].send_keys(pw)
    input_tag[2].send_keys("noah")
    sleep(time_interval)
    driver_agent.find_element(By.CLASS_NAME, 'btn').click()
    sleep(time_interval)

    driver_agent.find_element(By.CLASS_NAME, 'hexagon').find_element(By.TAG_NAME, 'img').click()
    sleep(time_interval)

    driver_agent.find_elements(By.CLASS_NAME, 'btn_unselsect')[8].click()
    sleep(time_interval)
    driver_agent.find_elements(By.CLASS_NAME, 'btn_unselsect')[7].click()
    sleep(time_interval)
    driver_agent.find_elements(By.CLASS_NAME, 'ivu-checkbox-input')[2].click()
    sleep(time_interval)
    driver_agent.find_element(By.CLASS_NAME, 'ivu-modal-confirm-footer').find_elements(By.TAG_NAME, 'button')[1].click()
    sleep(time_interval)
    driver_agent.find_elements(By.CLASS_NAME, 'btn_unselsect')[6].click()
    sleep(time_interval)
    button = driver_agent.find_elements(By.CLASS_NAME, 'ivu-btn-large')[1].find_element(By.TAG_NAME, 'span')

    while 1:
        if button.is_displayed():
            break
        sleep(1)
    button.click()

    sleep(1500)
    driver_agent.quit()


def main():
    users = {}
    csv_reader = csv.reader(open("./agent.csv"))

    count = start_user
    for line in csv_reader:
        users[count] = line
        count = count + 1

    for index in range(1, user_num + 1):
        print("this is agent user : ", users[index])
        sleep(concurrent_interval)
        _thread.start_new_thread(agent, (users[index][0], users[index][1],))
    sleep(20)
    for index in range(1, user_num + 1):
        print("this is client user : ", index)
        sleep(concurrent_interval)
        _thread.start_new_thread(client, ())
    while 1:
        pass


main()
