import pytest

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Scenario
scenarios('../features/login.feature')

# When
@when('I click login button')
def click_login_home_button(browser):
    button_login_home_id = browser.find_element_by_id('login_home')
    button_login_home_id.click()

# Then
@then('I should be on the Login form page')
def get_title(browser):
    title = browser.title
    # print(title)
    assert title == "Login - Female Daily"

# THen
@then('I should see the email text field')
def email_field_is_displayed(browser):
    email_field_id = browser.find_element_by_id('id-email-username')
    email_field_id.is_displayed()

# Then
@then('I should see the password text field')
def password_field_is_displayed(browser):
    password_field_id = browser.find_element_by_id('id-password')
    password_field_id.is_displayed()

# Then
@then('I should see login button')
def login_button_is_displayed(browser):
    login_button_xpath = browser.find_element_by_xpath('//input[@value="Login"]')
    login_button_xpath.is_displayed()

# Then
@then('I should be able to input my email address')
def input_email(browser):
    email_field_id = browser.find_element_by_id('id-email-username')
    email_field_id.send_keys('putwid')

# Then
@then('I should be able to input my password')
def input_password(browser):
    password_field_id = browser.find_element_by_id('id-password')
    password_field_id.send_keys('tester123')

# THen
@then('I click login button')
def click_login_button(browser):
    login_button_xpath = browser.find_element_by_xpath('//input[@value="Login"]')
    login_button_xpath.click()

# Then
@then('I should be see user home page')
def assert_user_homepage(browser):
    button_notification_id = browser.find_element_by_id('btn_login_navbar')
    button_notification_id.is_displayed()
