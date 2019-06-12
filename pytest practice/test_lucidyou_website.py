# content of test_lucidyou_website.py
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
users_added = []
subscribed = False


###################################################### Setup Module ######################################################
def setup_module(module):
    browser.maximize_window()
    browser.get("https://lucid-you.firebaseapp.com/")
    browser.implicitly_wait(10)

###################################################### Tear Down Moduel ######################################################
def teardown_module(module):
    global users_added, subscribed
    if subscribed == True:
        browser.get("https://lucid-you.firebaseapp.com/settings.html")
        time.sleep(1)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,"unSubscribeBtn"))).click()
        time.sleep(1)
    if len(users_added) != 0:
        #Get Rid of added users!
        browser.get("https://console.firebase.google.com/u/0/project/lucid-you/authentication/users")
        signin = browser.find_element_by_id("identifierId")
        submit = browser.find_element_by_id("identifierNext")
        signin.send_keys("lucid.you.example@gmail.com")
        submit.click()
        time.sleep(1)
        passwordElem = browser.find_element_by_name('password')
        passwordElem.send_keys("abc!@#123")
        passwordElem.submit()
        submit = browser.find_element_by_class_name("CwaK9")
        submit.click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "sort-by-created-at"))).click()
        for i in users_added:
            time.sleep(2)
            element_to_hover_over = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/ng-transclude/div/div/div/div/md-single-grid/md-card/div/table/tbody[2]/tr/td[6]/div/md-menu/button")
            hover = ActionChains(browser).move_to_element(element_to_hover_over)
            hover.perform()
            hover.perform()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/ng-transclude/div/div/div/div/md-single-grid/md-card/div/table/tbody[2]/tr/td[6]/div/md-menu/button"))).click()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/md-menu-content/md-menu-item[3]/button"))).click()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/md-dialog/div[3]/button[2]"))).click()
            #Need this sleep for Firebase to delete entry 
            time.sleep(4)
    browser.quit()


###################################################### Fixtures ######################################################
##Login Module
@pytest.fixture
def login():
    browser.get("https://lucid-you.firebaseapp.com/login.html")
    userName = browser.find_element_by_id("username").send_keys("test_suite@gmail.com")
    password = browser.find_element_by_id("password").send_keys("12345678")
    submit = browser.find_element_by_xpath("/html/body/main/button").click()
    time.sleep(2)

##SignupLink Module
@pytest.fixture(scope="module")
def signupPageLink():
    signupLink = browser.find_element_by_id("signup-link")
    signupLink.click()

##AddUser Module
@pytest.fixture(scope="module")
def AddUser():
    global browser, users_added   
    if len(users_added) == 0:
        user,password = "test_suite@gmail.com", 12345678
        browser.get("https://lucid-you.firebaseapp.com/signup.html")
        time.sleep(1)
        browser.find_element_by_id("txtEmail").send_keys(user)
        browser.find_element_by_id("txtPassword").send_keys(password)
        browser.find_element_by_id("txtPassword2").send_keys(password)
        browser.find_element_by_id("btnLogin").click()
        try:
            WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,"logout"))).click()
            users_added.append(user)
            time.sleep(2)
        except: 
            return False

##SignupPage Module
@pytest.fixture()
def signupPageSetup():
    browser.refresh()
    browser.implicitly_wait(10)
    userName = browser.find_element_by_id("txtEmail")
    password = browser.find_element_by_id("txtPassword")
    password2 = browser.find_element_by_id("txtPassword2")
    submit = browser.find_element_by_id("btnLogin")
    return (userName, password, password2, submit)

##Login page setup Module
@pytest.fixture()
def loginPageSetup():
    browser.get("https://lucid-you.firebaseapp.com/login.html")
    browser.implicitly_wait(10)
    userName = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    submit = browser.find_element_by_xpath("/html/body/main/button")
    return (userName, password, submit)

##Setup log dreams Module
@pytest.fixture
def setup_log_dreams():
    global browser, subscribed
    if subscribed is False:
        browser.get("https://lucid-you.firebaseapp.com/settings.html")
        time.sleep(2)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,"subscribeBtn"))).click()
        subscribed = True
        time.sleep(2)
    browser.get("https://lucid-you.firebaseapp.com/LogDreams.html")
    exp = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,"exp")))
    tags = browser.find_element_by_id("tags")
    sound1 = browser.find_element_by_id("sound1")
    sound2 = browser.find_element_by_id("sound2")
    freq1 = browser.find_element_by_id("freq1")
    freq2 = browser.find_element_by_id("freq2")
    amp1 = browser.find_element_by_id("amp1")
    amp2 = browser.find_element_by_id("amp2")
    rating = browser.find_element_by_id("rating")
    submit = browser.find_element_by_id("submit")
    return (exp, tags, sound1, sound2, freq1, freq2, amp1, amp2, rating, submit)

###################################################### Test Signup Page! ######################################################
# @pytest.mark.signup
@pytest.mark.parametrize('user, pass1, pass2, error, result', [
    ("me", "a", "b", "incorrect_password", "password doesn't match!"),
    ("me", "a", "a", "invalid", "This email is Invalid!"),
    ("", "12345678", "12345678", "invalid", "Invalid!"),
    ("me", "", "", "invalid", "email is"),
    ("test@gmail.com", "a", "a", "weak-pwd", "too weak!"),
    ("test_suite@gmail.com", 12345678, 12345678,"logged_in","Logged In as"),
    ("test_suite@gmail.com", 12345678, 12345678,"exists","This email is already registered!")
    ])
def test_signup(user, pass1, pass2, error, result, signupPageLink, signupPageSetup):
    global browser, users_added
    #Test the parameters    
    signupPageSetup[0].send_keys(user)
    signupPageSetup[1].send_keys(pass1)
    signupPageSetup[2].send_keys(pass2)
    signupPageSetup[3].click()
    try:
        #Some messages take a brief second to become visible
        element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, error)))
        #This will miss password too weak, needs to wait for it to become visible
        # element = browser.find_element_by_id(error)
    except:
        #If message takes too long to appear, then Fail test
        print("Took too long to appear, or no message!")
        assert False
    else:
        message = element.text
        print(message)
        assert result in message
        try:
            WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "logged_in"))).text
            WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,"logout"))).click()
            users_added.append(user)
            time.sleep(2)
            browser.get("https://lucid-you.firebaseapp.com/signup.html")
            # browser.back()
        except: pass



###################################################### Test Login Page ######################################################
# @pytest.mark.login
@pytest.mark.parametrize('user, password, result, error', [
    ("me", "a", "Wrong Credentials", "wrong"),
    ("me@gmail.com", "a", "Wrong", "wrong"),
    ("test_suite@gmail.com", "a", "Credentials", "wrong"),
    ("test_suite@gmail.com", 12345678,"test_suite@gmail.com","logged_in")
    ])
def test_login(user, password, result, error, AddUser, loginPageSetup):
    global browser
    loginPageSetup[0].send_keys(user)
    loginPageSetup[1].send_keys(password)
    loginPageSetup[2].click()
    try:
        if(error == "logged_in"):
            time.sleep(2)
        element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, error)))
    except:
        print("Took too long to appear, or no message!")
        assert False
    else:
        message = element.text
        print(message)
        assert result in message
    try:
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "logged_in"))).text
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID,"logout"))).click()
        browser.back()
    except: pass

###################################################### log dream logs tests ######################################################
@pytest.mark.parametrize('exp, tags, sound1, sound2, freq1, freq2, amp1, amp2, rating, site', [
    ("Had a great time last night, dreamt of angels", "angels, good sleep", "death metal", "things", "120", "121", "120", "230", "5", "LogDreams"),
    ("Had a great time last night, dreamt of angels", "angels, good sleep", "death metal", "things", "120", "121", "120", "230", "5", "forum"),
    ("Had a great time last night, dreamt of angels", "angels, good sleep", "death metal", "things", "120", "121", "120", "230", "5", "Records")
    ])
def test_log_dreams(login, exp, tags, sound1, sound2, freq1, freq2, amp1, amp2, rating, site, AddUser, setup_log_dreams):
    global browser, subscribed
    if site in browser.current_url:
        setup_log_dreams[0].send_keys(exp)
        setup_log_dreams[1].send_keys(tags)
        setup_log_dreams[2].send_keys(sound1)
        setup_log_dreams[3].send_keys(sound2)
        setup_log_dreams[4].send_keys(freq1)
        setup_log_dreams[5].send_keys(freq2)
        setup_log_dreams[6].send_keys(amp1)
        setup_log_dreams[7].send_keys(amp2)
        setup_log_dreams[8].send_keys(rating)
        setup_log_dreams[9].click()
        try:
            element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "loggedDream")))
        except:
            print("Took too long to appear, or no message!")
            assert False
        else:
            message = element.text
            print(message)
            assert "Logged" in message
            time.sleep(2)
    else:
        # if site == "forum" and subscribed is False:
        #     browser.get("https://lucid-you.firebaseapp.com/settings.html")
        #     time.sleep(1)
        #     WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,"subscribeBtn"))).click()
        #     subscribed = True
        #     time.sleep(10)
        if site == "forum":
            time.sleep(10)
        browser.get("https://lucid-you.firebaseapp.com/"+site+".html")
        assert sound1 in WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/records/div[1]/p[1]"))).text
        assert sound2 in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[2]").text
        assert freq1 in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[3]").text
        assert freq2 in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[4]").text
        assert amp1 in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[5]").text
        assert amp2 in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[6]").text
        assert rating in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[7]").text
        assert exp in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[8]").text
        assert tags in browser.find_element_by_xpath("/html/body/main/records/div[1]/p[9]").text
        if site == "Records":
            browser.find_element_by_xpath("/html/body/main/records/div[1]/button").click()
            time.sleep(1)