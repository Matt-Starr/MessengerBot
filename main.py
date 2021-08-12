from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv

def add_person(personId, reqestedGroup):
    with open('Resources\Grouplist.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    j = -1
    for i in data:
        j += 1
        print("i[0]", i[0])
        if i[0] == reqestedGroup:
            #open chat page and wait to load
            driver.get(i[1])
            print('i[1]', i[1])
            time.sleep(4)
            if i[2] == 'False':
                chatInput = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div')
                chatInput.send_keys("This is a calibration message")
                chatInput.send_keys(Keys.RETURN)
                time.sleep(1)
                driver.get(i[1])
                time.sleep(3)
                data[j][2] = 'True'
                with open('Resources\Grouplist.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(data)

            #navigate to add person box
            element = True
            i = 1
            while element:
                testxPath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div['+str(i)+']/div'
                if len(driver.find_elements_by_xpath(testxPath)) >= 1:
                    i += 1
                else:
                    xPath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div['+str(i-2)+']/div'
                    element = False
            addButton = driver.find_element_by_xpath(xPath)
            addButton.click()
            time.sleep(1)
            try:
                inputElement = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div/input")
                inputElement.send_keys(personId)
            except:
                #if chat has one extra drop down before add people button, close it and try the next spot up
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div['+str(i-2)+']/div').click()
                time.sleep(0.3)
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div['+str(i-3)+']/div').click()
                time.sleep(0.3)
                try:
                    inputElement = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div/input")
                    inputElement.send_keys(personId)
                except:
                    #if chat has two extra drop downs before add people button, close them both and try the next spot up
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div['+str(i-3)+']/div').click()
                    time.sleep(0.3)
                    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div['+str(i-4)+']/div').click()
                    time.sleep(0.3)
                    inputElement = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div/input")
                    inputElement.send_keys(personId)

            time.sleep(2)
            personToAddButton = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[3]/div/div[1]/div/div/div/div")
            personToAddButton.click()
            time.sleep(0.5)
            addPersonButton = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div")
            addPersonButton.click()
            return 0

#Open Messenger in a new window
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-data-dir=C:/Users/starr/AppData/Local/Google/Chrome/User Data");
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
driver.get("https://www.messenger.com")

#Wait until messenger loads up
time.sleep(6)
#Check every 10 seconds if there is someone waiting, if there is, add them to the group
while True:
    with open('Resources\Waitlist.csv', newline='') as f:
        reader = csv.reader(f)
        waitlist = list(reader)
        print(waitlist)
    if len(waitlist) > 0:
        personId = waitlist[0][0]
        requestedGroup = waitlist[0][1]
        print('personId',personId,'requestedGroup',requestedGroup)
        add_person(personId, requestedGroup)
        #remove person from wait list
        waitlist.pop(0)
        with open('Resources\Waitlist.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for i in waitlist:
                writer.writerow(i)
    else:
        time.sleep(5)
