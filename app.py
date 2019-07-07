import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_Keys(self.username)
        password.send_Keys(self.password)
        password.send_Keys(Keys.RETURN)
        time.sleep(3)


andrew = TwitterBot('username', 'password')
andrew.login()
