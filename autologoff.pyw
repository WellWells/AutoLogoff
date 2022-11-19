import ctypes
import json
import os
import time

user = "bo-xi"
logoff_time = 5
try:
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, 'setting.json'))
    data = json.load(f)
    user = data['user']
    logoff_time = data['afterTimeToLogoff']
    f.close()
except:
    print(
        "No setting.json. Please add setting.json. Example: {\"user\": \"bo-xi\",\"afterTimeToLogoff\": 900}")

print(user)
print(logoff_time)

if os.getlogin().lower().find(user) == 0:
    time.sleep(logoff_time)
    # ctypes.windll.user32.LockWorkStation()
    ctypes.windll.user32.ExitWindowsEx(0, 1)
