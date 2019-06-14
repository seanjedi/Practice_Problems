from  selenium import webdriver
from  selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest

browser = webdriver.Firefox()
repo_created = False

###################################################### Setup and Teardown Fictures ######################################################
@pytest.fixture(scope="module", autouse=True)
def web_driver():
    global browser
    browser.maximize_window()
    browser.get("https://github.com/login")
    login_field =  WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,"login_field")))
    password = browser.find_element_by_id("password")
    login_field.send_keys("lucid.you.example@gmail.com")
    password.send_keys("abc!@#123_3")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/main/div/form/div[3]/input[4]"))).click()
    yield
    global repo_created
    if repo_created is True:
        #remove the repository
        browser.get("https://github.com/test-suite/Test-Repo/settings")
        time.sleep(1)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div/div[2]/div/div[9]/ul/li[4]/details/summary'))).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div/div[2]/div/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input'))).send_keys("Test-Repo")
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div/div[2]/div/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button'))).click()
    browser.quit()

@pytest.fixture
def test_global_fixtures():
    print("THIS FIXTURE SHOULD BE CALLED EVERYWHERE")

###################################################### Setup Module ######################################################
# def setup_module(module):
#     browser.maximize_window()
#     browser.get("https://github.com/login")
#     login_field =  WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,"login_field")))
#     password = browser.find_element_by_id("password")
#     login_field.send_keys("lucid.you.example@gmail.com")
#     password.send_keys("abc!@#123_3")
#     WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/main/div/form/div[3]/input[4]"))).click()
#     yield
# ###################################################### Tear Down Moduel ######################################################
# def teardown_module(module):
#     global repo_created
#     if repo_created is True:
#         #remove the repository
#         browser.get("https://github.com/test-suite/Test-Repo/settings")
#         time.sleep(1)
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div/div[2]/div/div[9]/ul/li[4]/details/summary'))).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div/div[2]/div/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input'))).send_keys("Test-Repo")
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div/div[2]/div/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button'))).click()
#     browser.quit()

###################################################### Test Projects ######################################################
@pytest.mark.github_projects
# @pytest.mark.usefixtures("web_driver", "test_global_fixtures")
class Test_projects(object):
    def test_project_creation(self):
        #navigate to project creation, and click on the side menu to create tne project
        browser.get("https://github.com")
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/header/div[7]/details/summary"))).click()
        browser.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[5]").click()
        #insert into fields the project name and parameters
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="project_name"]'))).send_keys("Test for Github!")
        browser.find_element_by_xpath('//*[@id="project_body"]').send_keys("Testing the github project creation")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="project_public_true"]'))).click()
        browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button').click()
        #Test whether or not the project was created!
        assert "Test for Github" in WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div[4]/div[1]/div[2]/div/div/h3/span'))).text
        
        
    def test_project_column_creation(self):
        #click on button to create a column
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[2]/button'))).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="project-column-name-"]'))).send_keys("Testing")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/details/details-dialog/div/div[2]/form/dl[2]/dd[1]/div/div[1]/button'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/details/details-dialog/div/div[2]/form/dl[2]/dd[1]/div/div[2]/div/div[2]/div[2]'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/details/details-dialog/div/div[2]/form/div/button'))).click()
        assert "Testing" in WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[1]/div[1]/h4/span[2]'))).text

    def test_project_card_creation(self):
        #Test the creation of a card
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[1]/div[1]/button'))).click()
        browser.find_element_by_xpath('/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/form[1]/textarea').send_keys("test new card with abc")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[1]/div[2]/form[1]/div/button[1]'))).click()
        assert "test new card with abc" in WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/task-lists/div/p'))).text
        assert "Added by test" in browser.find_element_by_xpath('/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/small').text

    def test_project_card_edit(self):
        #Test editing a card!
        #This will go to the menu to edit the card, clear out the old string, and insert the new string and edit it
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/details/summary'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/details/details-menu/button'))).click()
        edit = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="card_note_text"]')))
        edit.clear()
        edit.send_keys("New String")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/details/details-dialog/div/div[2]/form/div/button'))).click()
        #Once card is done being edited, test the new card
        assert WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.XPATH,'/html/body/div[4]/main/div[4]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/task-lists/div/p'), 'New String'))

    def test_project_page_headings(self):
        #click on the projects tab, test where that brings us, and test that the project we created exists
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[1]/nav/a[2]'))).click()
        assert 'https://github.com/test-suite?tab=projects' == browser.current_url
        assert "Testing the github project" in WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/p'))).text

    def test_project_destruction(self):
        #Now close the project, and test if the project is gone, and that the projects closed is incremented
        num_closed = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/main/div/div[3]/div[4]/div/div[2]/div[1]/div[2]/a[2]'))).text
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/main/div/div[3]/div[4]/div/div[2]/div[2]/div/details/summary'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/main/div/div[3]/div[4]/div/div[2]/div[2]/div/details/details-menu/form/button'))).click()
        num_closed2 = browser.find_element_by_xpath('/html/body/div[4]/main/div/div[3]/div[4]/div/div[2]/div[1]/div[2]/a[2]').text
        num_closed = [int(s) for s in num_closed.split() if s.isdigit()]
        num_closed2 = [int(s) for s in num_closed2.split() if s.isdigit()]
        assert num_closed[0]+1 == num_closed2[0]



###################################################### Test Repositories ######################################################
@pytest.mark.github_repos
# @pytest.mark.usefixtures("web_driver", "test_global_fixtures")
class Test_repos(object):
    def test_repo_creation(self):
        global repo_created
        browser.get("https://github.com")
        #Create new repository
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/header/div[7]/details/summary'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/header/div[7]/details/details-menu/a[1]'))).click()

        #Insert Values
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,'repository_name'))).send_keys("Test Repo")
        browser.find_element_by_id('repository_description').send_keys("This is a test description")
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID,'repository_auto_init'))).click()
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/main/div/form/div[3]/button'))).click()
        repo_created = True
        #test creation
        init_file = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/main/div[2]/div[1]/div[8]/div[1]/h3'))).text
        repo_name = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.markdown-body > h1:nth-child(1)'))).text
        description = browser.find_element_by_css_selector('.markdown-body > p:nth-child(2)').text

        print(init_file)    
        print(repo_name)
        print(description)
        assert "README" in init_file
        assert "Test-Repo" in repo_name
        assert "is a test description" in description

    def test_repo_addfile(self):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/main/div[2]/div[1]/div[3]/div[2]/form/button'))).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/main/div[2]/div[1]/div/form[2]/div[1]/span/input'))).send_keys("Sample.txt")
        browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/div/form[2]/div[3]/div[2]/div/div[5]/div[1]').click()
        #open file and sned it to the code buffer
        file = open("sample.txt", "r")
        if file.mode == 'r':
            contents = file.read()
            ActionChains(browser).send_keys(contents).perform()
        else:
            assert False
        #After reading file is over, close file
        file.close()
        #submit the new file
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'submit-file'))).click()
        #check if the new file was submitted
        file_name = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/main/div[2]/div[1]/div[5]/table/tbody/tr[3]/td[3]/span/a')))
        print(file_name.text)
        assert "Create Sample" in file_name.text
        file_name.click()
        #test if the text was copied over, and matches the file
        text = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.blob-code-inner'))).text
        assert contents == text