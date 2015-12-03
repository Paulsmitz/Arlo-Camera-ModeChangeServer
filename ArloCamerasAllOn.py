# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from bottle import route, run, template
import unittest, time, re, os, threading


class workerThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "setting the display"
        os.environ["DISPLAY"] = ":99"
        print "Starting the Driver"
        driver = webdriver.Firefox()
        print "Waiting 5 secs for driver"
        driver.implicitly_wait(5)
        print "setting the base URL"
        base_url = "https://arlo.netgear.com/"
        print "Getting the Login Page"
        driver.get(base_url + "/#/login")
        print "clearing the login username"
        driver.find_element_by_id("userId").clear()
        print "setting the login username"
        driver.find_element_by_id("userId").send_keys("***USERNAME***")
        print "clearing the login password"
        driver.find_element_by_id("password").clear()
        print "setting the login password"
        driver.find_element_by_id("password").send_keys("***PASSWORD***")
        print "Logging in"
        driver.find_element_by_id("loginButton").click()
        for i in range(10):
            try:
                print "Waiting for the modes button to appear"
                if driver.find_element_by_xpath("//div[@id='footerButtonModes']").is_displayed():
                    break
            except: pass
            time.sleep(1)
        else:
            return

        print "hitting the modes button"
        driver.find_element_by_xpath("//div[@id='footerButtonModes']").click()
        print "Waiting for the arlo banner to disappear and to get modes"
        for i in range(3):
            time.sleep(1)

        if self.name == 'mode0':
            print "Mode0"
            driver.find_element_by_xpath("//div[3]/div[2]/div").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode1':
            print "Mode1"
            driver.find_element_by_xpath("//div[3]/div[2]/div[2]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode2':
            print "Mode2"
            driver.find_element_by_xpath("//div[2]/div[3]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode3':
            print "Mode3"
            driver.find_element_by_xpath("//div[4]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode4':
            print "Mode4"
            driver.find_element_by_xpath("//div[5]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode5':
            print "Mode5"
            driver.find_element_by_xpath("//div[6]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode6':
            print "Mode6"
            driver.find_element_by_xpath("//div[7]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode7':
            print "Mode7"
            driver.find_element_by_xpath("//div[8]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        elif self.name == 'mode8':
            print "Mode8"
            driver.find_element_by_xpath("//div[9]").click()
            driver.find_element_by_xpath("//span").click()
            driver.quit()
        else:
            print "No Mode"
            driver.find_element_by_xpath("//span").click()
            driver.quit()

        print "Changed the mode and logged out!"


@route('/<name>')
def index(name):
    thread = workerThread(1, name)
    thread.start()
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='0.0.0.0', port=8080)
