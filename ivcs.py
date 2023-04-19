import time
from telnetlib import EC

from pynput.keyboard import Key, Listener
import _thread
import os

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

clear_chrome = "taskkill /f /t /im chrome.exe"
os.popen(clear_chrome)


def network_listener():
    def network_open_close(key):
        close_network = "ipconfig /release"
        open_network = "ipconfig /renew"
        if key == Key.home:
            print("network close")
            os.popen(close_network)

        if key == Key.end:
            print("network open")
            os.popen(open_network)

    with Listener(on_press=network_open_close) as listener:
        listener.join()


agent_url = "https://ivcs-test-k8s-azure.zealcomm.cn"
# agent_url = "https://ivcs-demo.zealcomm.cn"
client_url = agent_url + "/customer/"


class agent_data:
    def __init__(self, username, password, mechanism):
        self = self
        self.username = username
        self.password = password
        self.mechanism = mechanism


class client_data:
    def __init__(self, username, mechanism):
        self = self
        self.username = username
        self.mechanism = mechanism
def create_driver():
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
    ch_option.add_argument("--disable-infobars")
    # ch_option.add_argument('--headless')
    # ch_option.add_argument('--disable-cpu')

    driver = webdriver.Chrome(options=ch_option)
    # driver = webdriver.Chrome(os.path.join(sys._MEIPASS, 'driver', 'chromedriver.exe'))
    # driver = webdriver.Chrome(os.path.join(sys._MEIPASS, 'driver', 'chromedriver.exe'), options=chrome_options)
    driver.implicitly_wait(10)
    return driver

def agent(user):
   
    print("agent start")
    driver = create_driver()
    print(agent_url)
    driver.get(agent_url)
    data = driver.find_elements(By.TAG_NAME, "input")
    data[0].send_keys(user.username)
    data[1].send_keys(user.password)
    data[2].send_keys(user.mechanism)
    driver.find_element(By.TAG_NAME, "button").click()
    driver.find_elements(By.CLASS_NAME, "iconfont")[2].click()
    driver.find_elements(By.CLASS_NAME, "ant-switch")[0].click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "ant-modal-mask"))
    )
    driver.find_elements(By.CLASS_NAME, "ant-checkbox-input")[0].click()
    driver.find_elements(By.CLASS_NAME, "ant-btn-primary")[0].click()
    driver.find_elements(By.CLASS_NAME, "ant-switch")[1].click()
    # 等待通话接通
    WebDriverWait(driver, 999).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-box"))
    )
    driver.find_elements(By.CLASS_NAME, "ant-btn-primary")[1].click()
    print("agent over")

    def network_agent(key):
        close_network = "ipconfig /release"
        open_network = "ipconfig /renew"
        if key == Key.page_up:
            print("network close")
            driver.set_network_conditions(
                latency=0,
                offline=True,
                download_throughput=500 * 1024,
                upload_throughput=500 * 1024)
        if key == Key.page_down:
            print("network open")
            driver.set_network_conditions(
                latency=0,
                offline=False,
                download_throughput=500 * 1024,
                upload_throughput=500 * 1024)

    with Listener(on_press=network_agent) as listener:
        listener.join()
    sleep(10000)


def client(user):
    print("client start")
    driver = create_driver()
    # 打开新的标签页
    driver.get(client_url)
    data = driver.find_elements(By.TAG_NAME, "input")
    data[0].send_keys(user.username)
    data[1].send_keys(user.mechanism)
    driver.find_element(By.CLASS_NAME, "loginbtn").click()
    driver.find_elements(By.CLASS_NAME, "picimage")[1].click()
    driver.find_element(By.TAG_NAME, "button").click()
    # WebDriverWait(driver, 999).until(
    #     expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-box"))
    # )
    sleep(1)
    # driver.find_elements(By.CLASS_NAME, "ivu-dropdown-item")[0].click()
    driver.find_elements(By.CLASS_NAME, "ivu-dropdown-item")[6].click()
    driver.find_elements(By.CLASS_NAME, "ivu-select-placeholder")[0].click()
    driver.find_elements(By.CLASS_NAME, "ivu-select-item")[0].click()
    driver.find_elements(By.CLASS_NAME, "defaultbackColor")[0].click()
    print("client over")
    # sleep(10)
    # driver.quit()

    # def network_agent(key):
    #     if key == Key.up:
    #         print("network close")
    #         driver.set_network_conditions(
    #             latency=0,
    #             offline=True,
    #             download_throughput=500 * 1024,
    #             upload_throughput=500 * 1024)
    #     if key == Key.down:
    #         print("network open")
    #         driver.set_network_conditions(
    #             latency=0,
    #             offline=False,
    #             download_throughput=500 * 1024,
    #             upload_throughput=500 * 1024)

    # with Listener(on_press=network_agent) as listener:
    #     listener.join()
    sleep(10000)


def manage():
    print("manage start")
    driver = create_driver()

    sleep(2)
    js = "window.open('" + agent_url + "')"
    driver.execute_script(js)


def mian():
    user1 = agent_data("001", "123456", "noah")
    user2 = agent_data("002", "123456", "noah")
    client1 = client_data("001", "noah")
    _thread.start_new_thread(agent, (user2,))
    sleep(4)
    # _thread.start_new_thread(agent, (user2,))
    _thread.start_new_thread(client, (client1,))
    _thread.start_new_thread(network_listener, ())
    sleep(10000)


mian()
