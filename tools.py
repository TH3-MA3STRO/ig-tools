import glob
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import requests
import bs4
import re
import json


# Spam details
msg = "Wow cool post thanks for sharing!"


def tag_based(u_name, pass_w, w0hash):
    driver = webdriver.Chrome(executable_path=r'''/home/chromedriver''')
    wait = WebDriverWait(driver, 40)
    #Logging in
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    driver.find_element_by_xpath("//input[@name='username']").send_keys(u_name)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(pass_w)
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='Log In']").click()
    time.sleep(10)
    print("Logged in...")
    # Closing the 'Turn on notifications pop-up'
    driver.find_element_by_xpath("//div[@class='mt3GC']/button[@class='aOOlW   HoLwm ']").click()
    num_j = 0
    print(w0hash)
    if len(w0hash) >= 4:
        num_j = 4
    else:
        num_j = num_j + len(w0hash)

    # Spamming part starts from here
    for i in range(0, num_j):
        time.sleep(5)
        driver.get("https://www.instagram.com/explore/tags/{}/".format(w0hash[i]))
        time.sleep(3)
        time.sleep(2)

        # The first post in the tag
        first_thumb = driver.find_element_by_xpath("//body/span/section/main/article/div[1]/div/div[1]/div[1]/div[1]")
        first_thumb.click()

        try:  # Wait until comment box is clickable
            wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@class='Ypffh']")))
            c_box = driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@aria-label='Comment']")

        except selenium.common.exceptions.StaleElementReferenceException:
            wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@class='Ypffh']")))
            c_box = driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@aria-label='Comment']")

        try:
            like = driver.find_element_by_xpath(
                "//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
            like.click()
        except selenium.common.exceptions.WebDriverException:
            pass

        # Next button
        

        for z in range(0, 3):
            time.sleep(1)

            try:
                try:
                    c_box.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    pass
                time.sleep(1)
                pyautogui.typewrite(msg)
                time.sleep(1)
                pyautogui.typewrite(['enter'])

                try:  # Goto next post
                    next_btn = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
                    next_btn.click()
                except selenium.common.exceptions.StaleElementReferenceException:
                    pyautogui.alert("Some error occured or you've reached the last post", timeout=7000)
                    pyautogui.alert("Exiting.......", timeout=5000)

                    
                time.sleep(2)

            except selenium.common.exceptions.ElementClickInterceptedException:
                pass

            wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@class='Ypffh']")))
            c_box = driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@aria-label='Comment']")

            try:
                like = driver.find_element_by_xpath(
                    "//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
                like.click()
            except selenium.common.exceptions.WebDriverException:
                pass
        time.sleep(4)


def profile(u_name, pass_w, tar_uname):
    driver = webdriver.Chrome(executable_path=r'''/home/chromedriver''')
    wait = WebDriverWait(driver, 40)

    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
    driver.find_element_by_xpath("//input[@name='username']").send_keys(u_name)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(pass_w)
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='Log In']").click()
    time.sleep(10)
    print("Logged in...")
    # Closing the 'Turn on notifications pop-up'
    driver.find_element_by_xpath("//div[@class='mt3GC']/button[@class='aOOlW   HoLwm ']").click()

    driver.get("https://www.instagram.com/{}/".format(tar_uname))
    time.sleep(4)
    first_thumb = driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/div/article/div[1]/div/div[1]/div[1]/a/div")
    first_thumb.click()
    try:  # Wait until comment box is clickable
        wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@class='Ypffh']")))
        c_box = driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@aria-label='Comment']")

    except selenium.common.exceptions.StaleElementReferenceException:
        print('c_box found at line 71')
        wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@class='Ypffh']")))
        c_box = driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@aria-label='Comment']")

    try:  # Wait until like button is clickable
        like = driver.find_element_by_xpath(
            "//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
        like.click()
    except selenium.common.exceptions.WebDriverException:
        print("Post Already liked or some other error...")
    # next Arrow button
    next_btn = driver.find_element_by_xpath("//a[@class='HBoOv coreSpriteRightPaginationArrow']")
    # for loop so it either spams all the post until it reaches the last post, or the top 20 posts only, but you can
    # change these
    for zzz in range(0, 20):

        time.sleep(1)

        try:
            try:
                c_box.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                pass
            time.sleep(1)
            pyautogui.typewrite(msg)
            time.sleep(1)
            pyautogui.typewrite(['enter'])

            try:  # Goto next post
                next_btn.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                pyautogui.alert("Some error occured or you've reached the last post", timeout=7000)
                pyautogui.alert("Exiting.......", timeout=5000)

                break
            time.sleep(2)

        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@class='Ypffh']")))
        c_box = driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@aria-label='Comment']")

        try:
            like = driver.find_element_by_xpath(
                "//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
            like.click()
        except selenium.common.exceptions.WebDriverException:
            print("Post Already liked or some other error...")


def _geturl(username):
    url = 'https://www.instagram.com/{}'.format(username)
    page = requests.get(url)
    if page.status_code == 200:
        soup = bs4.BeautifulSoup(page.text,'lxml')
        scrpt = soup.find('script',text= re.compile("window._sharedData")).text.replace('window._sharedData = ','')
        scrpt = json.loads(scrpt.replace(';',''))['entry_data']['ProfilePage'][0]['graphql']['user']
        print("***ACCOUNT DETAILS***\nFull name: {}\nFollowers: {}\nFollowing: {}\nPrivate: {}".format(scrpt['full_name'],scrpt['edge_followed_by']['count'],scrpt['edge_follow']['count'],scrpt['is_private']))
        return scrpt['profile_pic_url_hd']
    else:
        pass


def _getdp(url, fname):
    img = requests.get(url, stream=True)
    with open(fname, 'wb') as f:
        f.write(img.content)
    print('SUCCESS! IMAGE SAVED IN FILE: '+fname)


def execute(username):
    fname = username+'.jpg'
    url = _geturl(username)
    if url != None:
        dp = _getdp(url,fname)
    else:
        print('USER DOES NOT EXISTS')
