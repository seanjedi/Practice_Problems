# content of test_sample.py
import pytest

def func(x):
    return x + 1

# @pytest.mark.skip(reason = "debug mode")
# def test_answer():
#     assert func(4) == 5

############Fixture
@pytest.fixture(scope="module")
def fix():
    print ("HI!")
    yield 1
    print("BYE!!!")

#################Setup and Teardown
# def setup_module(module):
#     print ("hi")

# def teardown_module(module):
#     print ("Bye!")

#############Tests
@pytest.mark.tests
def test_fixture(fix):
    assert fix+1 == 2

# def test_fixture2(fix):
#     assert fix+2 == 3

# @pytest.mark.parametrize('num, num2, result', [(1, 2, 3),(2, 3, 5)])
# def test_strings(num, num2, result):
#     assert num + num2 == result


############# Scikit-learn
#"""Scikit-learn (formerly scikits.learn) is a free software machine learning library for the Python programming language.
# It features various classification, regression and clustering algorithms including support vector machines, random forests,
#  gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries
#  NumPy and SciPy."


#################### remove a file
#import os
# Delete file test2.txt
#os.remove("text2.txt")
# Create a directory "test"
# os.mkdir("test")