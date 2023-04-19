import requests
import time
def main():
    print("start")
    url = 'https://music.163.com/#/discover/toplist'
    # 发送get请求，获取响应对象
    response = requests.get(url)
    time.sleep(1)
    print(response.text)
main()