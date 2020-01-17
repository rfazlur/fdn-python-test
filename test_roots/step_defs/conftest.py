import pytest

from test_roots.util import constans
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given


# Constans
# FEMALEDAILY_HOME = 'https://femaledaily.com/'

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'step failed: {step}')


# Fixture
@pytest.fixture
def browser():
    b = webdriver.Chrome(ChromeDriverManager().install())
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given
@given('I load the female daily web application')
def fdn_home(browser):
    browser.get(constans.FEMALEDAILY_HOME)
