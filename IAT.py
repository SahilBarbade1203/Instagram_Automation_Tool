from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random


listofcomment = ["Just when I couldn’t love you more.","You posted this pic, and my jaw dropped to the floor."," The stars, the moon, and the sun are minor to me since you sparkle brighter than all of them."," Your beauty is one of the things I like about you."," There are endless possibilities for your beauty. Beauty is just one of the beautiful features you have."," Behind those beautiful eyes lies a fascinating story. This is the most remarkable thing I have seen today. This picture is astounding."," You look pretty gorgeous; please stop looking so beautiful every time."," You are a natural beauty; you do not need make-up yet."," Your hair just adds extra beauty to your gorgeousness."," Oh, you little girl, you stole my heart."," Do you have a brighter shade of lipstick because the current one doesn’t go with that dazzling smile of you?"," You are like sunshine when it is raining in my life."," Astonishingly lovable and natural beauty with lots of tremendous charm and fantastic gorgeousness."," I had never seen true beauty until this day."]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com')
sleep(5)

username_element = driver.find_element("name","username")
username_element.send_keys("Sdmr_1203")
password_input = driver.find_element("name", "password")
password_input.send_keys("Sahil121#")
login = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
login.click()
sleep(15)
notnow = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
notnow.click()
sleep(10)
nonotification = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")
nonotification.click()
driver.get("https://www.instagram.com/explore/tags/birds/")
sleep(10)
follow = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/header/div[2]/div/button")
follow.click()
sleep(3)
post = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a")
post.send_keys()
post.click()
sleep(5)
for i in range(1,20,1):

    like = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
    like.click()
    sleep(1)
    polygon = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/div/button")
    polygon.click()
    sleep(3)
    comment = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
    comment.click()
    comment = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
    comment.click()
    comment.send_keys(random.choice(listofcomment))
    sleep(3)
    postit = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div[2]/div")
    postit.click()
    sleep(1)
    next = driver.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")
    next.click()
    sleep(4)

sleep(30)


