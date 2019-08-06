from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium
import time
import pyautogui


def replay():
    return pyautogui.confirm("Click Ok if you want to spam again!")


driver = webdriver.Chrome(executable_path=r'''/home/chromedriver''')

action = ActionChains(driver)

u_name = 'imperial_d3ads3c'
passw = 'Sj00000'
msg = "Wow cool post thanks for sharing!"


driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(7)
driver.find_element_by_xpath("//input[@name='username']").send_keys(u_name)

driver.find_element_by_xpath("//input[@name='password']").send_keys(passw)
time.sleep(2)
driver.find_element_by_xpath("//div[text()='Log In']").click()
time.sleep(10)
pyautogui.alert()
while True:

    try:
        #

        like = driver.find_elements_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")


        for i in like:
            time.sleep(2)
            i.click()
            time.sleep(2)
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        like = driver.find_elements_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
        time.sleep(1)

    except selenium.common.exceptions.WebDriverException:
        break


