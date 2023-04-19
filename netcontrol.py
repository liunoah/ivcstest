
from pynput.keyboard import Key, Listener
import os
ipconfig = "C:\Windows\System32\ipconfig.exe"
def network_open_close(key):
    close_network = ipconfig + " /release"
    open_network = ipconfig + " /renew"
    if key == Key.home:
        print("network close")
        os.popen(close_network)

    if key == Key.end:
        print("network open")
        os.popen(open_network)

with Listener(on_press=network_open_close) as listener:
    listener.join()
