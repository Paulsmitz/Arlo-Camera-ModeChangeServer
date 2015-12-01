# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from bottle import route, run, template
import unittest, time, re, os

@route('/<name>')
def index(name):
    os.environ["DISPLAY"] = ":99"
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    base_url = "https://arlo.netgear.com/"
    accept_next_alert = True
    driver.get(base_url + "/#/login")
    driver.find_element_by_id("userId").clear()
    driver.find_element_by_id("userId").send_keys("*** USERNAME ***")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("*** PASSWORD ***")
    driver.find_element_by_id("loginButton").click()
    
    for i in range(10):
        try:
            if driver.find_element_by_xpath("//div[@id='footerButtonModes']").is_displayed():
                break
        except: pass
        time.sleep(1)
    else:
        return template('<b>Sorry {{name}}</b>!', name=name)
    driver.find_element_by_xpath("//div[@id='footerButtonModes']").click()

    for i in range(3):
        time.sleep(1)

    if name == 'mode0':
        driver.find_element_by_xpath("//div[3]/div[2]/div").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode1':
        driver.find_element_by_xpath("//div[3]/div[2]/div[2]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode2':
        driver.find_element_by_xpath("//div[2]/div[3]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode3':
        driver.find_element_by_xpath("//div[4]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode4':
        driver.find_element_by_xpath("//div[5]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode5':
        driver.find_element_by_xpath("//div[6]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode6':
        driver.find_element_by_xpath("//div[7]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode7':
        driver.find_element_by_xpath("//div[8]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    elif name == 'mode8':
        driver.find_element_by_xpath("//div[9]").click()
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Hello {{name}}</b>!', name=name)
    else:
        driver.find_element_by_xpath("//span").click()
        driver.quit()
        return template('<b>Sorry {{name}}</b>!', name=name)


run(host='0.0.0.0', port=8080)
