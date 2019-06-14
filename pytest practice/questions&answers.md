# Homework Questions
## 1) What is the methods of calling a function before every testcase
One way to do this is to create a test class, and call utilize: `@pytest.mark.usefixtures("web_driver", "test_global_fixtures")`

IE:

    @pytest.mark.usefixtures("web_driver", "test_global_fixtures")
    class Test_repos(object):
    def test_repo_creation(self):
    ..........`
Another way to do this is by using auto use
Occasionally, you may want to have fixtures get invoked automatically without declaring a function argument explicitly or a usefixtures decorator
IE:

    @pytest.fixture(scope="module", autouse=True)
    def fixture_created():
    .....Rest of Fixture definition...

## 2) Why does certain browser.find_element fail unless if there is a time.sleep(), and why doesn't implicit waits wait for 10 seconds to fix this?
It fails when I do implicit waits since it doesn’t wait for a certain condition of the element to occur before proceeding with finding the element, which in this case is for the element to be visible with the correct items in it. 
For implicit wait, it just waits for the element to be available on the DOM, but it might not be in the right state for it to be read. While inputting time.sleep(), it corrects the issue by waiting for it to be in the right state, but this could also be better done with explicit waits with expected conditions such as element_to_be_clickable or visibility_of_element_located.
Below is the selenium documentation descriptions of both

**Implicit Wait:** implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available

**Explicit Wait:** explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. It polls the condition every 500 milliseconds until the condition is met.

**As someone on stack overflow puts it**: The best solution would be to remove all the instance of `implicitly_wait(time_to_wait)` and replace with `WebDriverWait()` for a stable behavior of the _Application Under Test (AUT)_.

## 3) Why doesn't the action chains work every single time in my application?
I believe in my example, action chains weren’t working since the element that it was searching for wasn’t initialized correctly on the DOM yet, and it needed some time to setup into the right location.
 
**As someone on Stack overflow puts it:** “You need to do this step by step _checking the visibility of the elements_ you are going to interact with using Explicit Waits, do not use `time.sleep()` - it is not reliable and error-prone:”

## 4) How to parameterize the code to specify the website, either from a config file or the command line
To do this from the command line, we could utilize a string parser into our config file, that searches for a string on the command line, and if it is present, then it parses the website and injects it into the the test we want. One example of this is changing the website that we may want, and to do this we can create a parser within conftest.py such as:

    def pytest_addoption(parser):
	    parser.addoption(
		    "--website",
		    action="store",
		    nargs='*',
		    default=["https://docs.pytest.org/en/latest/contents.html"],
		    help="list of stringinputs to pass to test functions"
	    )
	    
    def pytest_generate_tests(metafunc):
	    if  "website"  in metafunc.fixturenames:
		    metafunc.parametrize("website", metafunc.config.getoption("website"))

This also has a default value, which in this case will direct us to the documents page for Pytest, but if we specify a new page inside our command line, that will overwrite the default value and bring us to that page instead. The command line code will look like this:

    pytest .\test_strings.py --website="https://www.google.com"

If we want to append to the default list instead, we would change action from store to append, and remove nargs (since nargs would remove the default right now). We then could do something like below, and test multiple websites including the default one:

    pytest .\test_strings.py --website="https://www.google.com" --website="https://stackoverflow.com/"

And inside our test function we would have the following to get the value from the parser:

    def test_valid_string(website):
	    browser = webdriver.Firefox()
	    browser.get(website)
	    assert website in browser.current_url
	    browser.quit()
Another way of doing this is to add a list of parameters within the test program, and read in the parameters from within the file and parameterize the test case:

    testdata = [
	    "https://www.google.com",
	    "https://stackoverflow.com/"
    ]
    
    @pytest.mark.parametrize("webpage", testdata)
	    def test_webpage(webpage):
	    browser = webdriver.Firefox()
	    browser.get(webpage)
	    assert webpage in browser.current_url
	    browser.quit() 
But if you want to have your list of parameters within the conftest.py file so that you can use it within multiple files and have only one file to change if you want to change the website list, then you can send in the parameters from a fixture inside the conftest.py file like so:
**conftest.py**

    testdata = [
	    "https://www.google.com",
	    "https://stackoverflow.com/"
    ]
    
    @pytest.fixture(params=testdata)
    def webpage(request):
	    param = request.param
	    return param

**test_parameters.py**

    def test_webpage_conftest(webpage):
	    browser = webdriver.Firefox()
	    browser.get(webpage)
	    assert webpage in browser.current_url
	    browser.quit()

## 5) How to skip a test from the command line
To do this, you could use -k and specify to not evoke the exact test case.
IE: `pytest -k 'not test_signup'`
This also works for test classes, so if I have an entire class called Test_repos, then I can skip the whole suite of testcases with:

    pytest -k 'not Test_repos'

## 6) Create an pytest.ini file and create marks for the tests
To create an pytest.ini file with markers for tests, all you need to do is add the [pytest] header and after that have a tile for markers, with the markers indented on the following lines. The information after the : is optional.

    [pytest]
    markers = 
	    signup: "Test the signup of a user in Lucid You"
	    login: "Test the login of a user in Lucid You"
	    log_dreams: "Testes the recording function within Lucid You"
	    github_repos: "Tests the repositories and functions within github"
	    github_projects: "Tests the projects within github"

## 7) How to mark all the tests, without going to each one to mark them
What you could do is create a test class, and mark that at the beginning. IE if I wanted to make a class for github repos, and I wanted it to be marked, I can make it with this:

    @pytest.mark.github_projects
    class Test_projects(object):
	    def test_project_creation(self):
	    ...........
What this will do is put the markers to each and every test case within this test class/suite

## Optional: What are alternative methods I could use to find a specific element on a webpage, not using Absolute XPath
The other locators available in Selenium are:
 1. **Locating by ID:** the first element with the id attribute value matching the location will be returned. Might be the best method to find an element, since ids should be unique.
 2. **Locating by name**: The first element with the name attribute value matching the location will be returned. Might be a really great method to use if the name is unique, might have some trouble if there is multiple names.
 3. **Locating by tag name:** Will give me the first element with that tag, if the tag is unique this is good, but this might be too general
 4. **Class Name**: the first element with the matching class attribute name will be returned
 5. **CSS Selector** With this strategy, the first element with the matching CSS selector will be returned
 6. **Relative/related XPath:** The problem with using the absolute XPATH is that they are likely to fail with only the slightest adjustment to the application. By finding a nearby element with an id or name attribute (ideally a parent element) you can locate your target element based on the relationship. This is much less likely to change and can make your tests more robust. This could be done with finding the first relative elements, such as if we were looking for the first element in a form, we could write: *//form[1]*. For a specific id in a form, we can write: *//form[@id='specific item']*.  And for specific names within a tag, we could use something like *//tag[@name='Element Name']*. 

## Optional: sharing a fixture instance across tests in a class, module or session
Fixtures requiring network access opening databases depend on connectivity and are usually time-expensive to create. In order to prevent reopening a network, and to share the same one, we can add a `scope="module"` parameter to the `@pytest.fixture` invocation to cause the decorated fixture function to only be invoked once per test _module_ (the default is to invoke once per test _function_). Multiple test functions in a test module will thus each receive the same fixture instance, thus saving time.
Possible values for `scope` are: `function`, `class`, `module`, `package` or `session`.
