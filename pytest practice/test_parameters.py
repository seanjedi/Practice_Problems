# content of test_strings.py
from  selenium import webdriver
from  selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest

testdata = [
    "https://www.google.com",
    "https://stackoverflow.com/"
]

def test_valid_string(website):
    browser = webdriver.Firefox()
    browser.get(website)
    assert website in browser.current_url
    browser.quit()


@pytest.mark.parametrize("webpage", testdata)
def test_webpage(webpage):
    browser = webdriver.Firefox()
    browser.get(webpage)
    assert webpage in browser.current_url
    browser.quit()

def test_webpage_conftest(webpage):
    browser = webdriver.Firefox()
    browser.get(webpage)
    assert webpage in browser.current_url
    browser.quit()