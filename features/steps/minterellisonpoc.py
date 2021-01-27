from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*
from selenium import webdriver
from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("Automation started on:", dt_string)

@given(u'Go to Test URL')
def step_impl(context):
    context.browser.get(database.userdata["testurl"])
    sleep(3)

@when(u'Homepage is displayed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.img_logo).is_displayed()
    context.browser.find_element(By.XPATH,locator.hamburger_menu).is_displayed()
    context.browser.find_element(By.XPATH,locator.solr_search_box).is_displayed()
    sleep(1)

@then(u'Validate homepage')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.homepage_header).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.homepage_header)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["homepage_header"]))
    sleep(1)
    context.browser.find_element(By.XPATH,locator.thumbnail_title_item1).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.thumbnail_title_item1)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["thumbnail_title_item1"]))
    sleep(1)
    context.browser.find_element(By.XPATH,locator.footer_copyright_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.footer_copyright_text)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["footer_copyright_text"]))
    sleep(3)

@then(u'Perform a search')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.solr_search_box).click()
    context.browser.find_element(By.XPATH,locator.solr_search_box).send_keys(database.userdata["search_keyword"])
    sleep(3)

    element = context.browser.find_element(By.XPATH,locator.autocomplete_item1)
    hov = webdriver.ActionChains(context.browser).move_to_element(element)
    hov.perform()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.autocomplete_item1).click()
    sleep(3)

@then(u'Validate search result')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.global_search_header).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.global_search_header)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["global_search_header"]))
    sleep(1)
    context.browser.find_element(By.XPATH,locator.global_time_list).is_displayed()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.global_author_list).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.global_author_list)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["global_author_list"]))
    sleep(3)
