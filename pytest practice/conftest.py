import pytest

testdata = [
    "https://www.google.com",
    "https://stackoverflow.com/"
]


def pytest_addoption(parser):
    parser.addoption(
        "--website",
        action="append",
        # nargs='*',
        default=["https://docs.pytest.org/en/latest/contents.html"],
        help="list of stringinputs to pass to test functions"
    )

def pytest_generate_tests(metafunc):
    if "website" in metafunc.fixturenames:
        metafunc.parametrize("website", metafunc.config.getoption("website"))

@pytest.fixture(params=testdata)
def webpage(request):
    param = request.param
    return param