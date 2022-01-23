from selenium import webdriver
import os
import time
import requests
from selenium.webdriver.common.keys import Keys
import shutil
import base64
import io
from PIL import Image
os.chdir(r"D:\Trees\Healthy Trees")
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\pianb\Downloads\Python\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get(r"http://www.google.com")
search = driver.find_element_by_name('q')
search.send_keys('ash tree bark identification',Keys.ENTER)
elem = driver.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()
value = 0
i = 0
for i in range(2000):
	driver.execute_script('scrollBy("+ str(value) +",+500);')
	value += 100
	print(i)
elements = driver.find_elements_by_xpath('//img[contains(@class,"rg_i")]')
count = 0
print("done")
for i in elements:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            count+=1
            print(src)
            if("data:image/jpeg;base64" in src):
                z = src[src.find(b'/9'):]
                im = Image.open(io.BytesIO(base64.b64decode(src))).save('{}.jpg'.format(time.time()))
            else:
                filename = ("Tree"+str(time.time())+".jpg")
                r = requests.get(src, stream=True)
                r.raw.decode_content = True
                with open(filename, 'w+b') as f:
                    shutil.copyfileobj(r.raw, f)
            if count%1000 == 0: 
                print("downloaded",count,"images")
        else:
            raise TypeError
    except TypeError:
        pass
