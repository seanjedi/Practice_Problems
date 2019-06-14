# Explanation on Files
## test_lucidyou_website.py
The purpose of this test suite is to test different parts of my senior design website, Lucid You.
I have 3 important parts fields in which I want to test, signing up a user, the login page, and the ability to add to the dream journal.
### Setup
For the setup fixture of this test suite, setup opens up the page, and maximizes the window. 

### Fixtures
**AddUser:** Adds a test user if one doesn't exist yet
**Login: logs:** the test user in (Should be called after AddUser is created)
**signupPageLink:** Brings user to the signup page
**signupPageSetup:** Setups the locators for Signup page to make some tests have less redundancy
**loginPageSetup:** Sets up locators for login page
**setup_log_dreams:** Sets up locators for log dreams page

###  Test Signup Page!
**test_signup:** Tests the signup page, each parameter should either have an incorrect combination of a password, that will trigger different error responses. 
There should be one test that successfully creates a user, and automates them to log off
Finally there is a test to try to create a user that already exists, and should come up with the error: *This email is already registered!*

### Test Login Page
**test_login:** This module tests different incorrect credentials to the field, and whether or not the correct error message appears.
It finally tests a correct login, in which a user is logged in and then decides to log off.

### log dream logs tests
**test_log_dreams:** There is 3 main portions of this test:
*One:* To test the creation of a user on the log dreams page, and if the right message appears. It inserts text on the input fields, and clicks submit. The problem with this website is that you can input any field with any value, and once you hit submit it will create a log, even if its empty. So there isn't much to test here

*Two:* To test if signing up for the forum and once that happens if the log appears in the forum. This test is a bit unstable, since there seems to be a race condition before the forum updates and when the program checks. Sometimes it passes, and sometimes the old value persists for a long time. More of a problem on how long Firebase updates the values.

*Three:* To test whether or not the log appears in the user records, and whether or not the user is capable of removing the created log

### Tear-down
For tear-down fixture, I have it so that it unsubscribes a user from the forum if they signed up for it, and I have to go to the Firebase database to remove a user. Unfortunately, I left out features while creating this project due to the client's intent, one of those features removed is the ability to go to settings and to remove yourself as a user. In order to do that, you would need to ask the website admins, and they may do that for you. In my case, i automated a login for one of the admins, and automated a way to remove the newly added test user if one was added.

## test_github.py
There is no fixtures in this program, but some supporting files in which I read from to do some testing of file insertion later. I will describe the sample.text below.
### setup_module
The setup ficture automates the login for Github with the test user I setup for these tests
### Test Projects
**test_project_creation:** Tests the creation of a project within github, and whether or not the project created has the correct name.
**test_project_column_creation:** Creates a column, and tests if that column created is correct
**test_project_card_creation:** creates a card in the column, and tests whether or not that card is correct
**test_project_card_edit:** Tests the edit function for a card in Github, and whether or not the edit was successful in changing the card title.
**test_project_page_headings:** Goes to the projects tab inside Github, with the list of all the projects we created. Checks if the project we created is present.
**test_project_destruction:** Removes the project we created, and checks if it is gone, and if the projects closed counter increments.
### Test Repositories
**test_repo_creation:** Creates a repository within github, and checks if the repo's name and description is correct.
**test_repo_addfile:** Adds a new file to the repository we just created, and tests if the file was created, and if the name and contents are correct.
### teardown_module
The tear-down fixture for these tests removes a repository if one is created, and closes the browser
### sample.txt
The sample text i have for these tests are only used for the repository testing, and contains a short verse from the sample text lorem ipsum found online.


## out.txt
This file is an example output of my test cases running: 
*pytest -v > out.txt*
it fails at one point with a function inside test_lucidyou_website.py due to a race condition for one of the tests with test_log_dreams. Aside from that, everything else passes
