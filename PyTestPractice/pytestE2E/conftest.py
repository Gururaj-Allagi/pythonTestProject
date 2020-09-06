import pytest


@pytest.fixture(scope="class")
def setup():
    print("\n1st")
    yield
    print("last  ")


@pytest.fixture()
def dataLoad():
    print("UN, PWD")
    return ["Gururaj", "Allagi"]


@pytest.fixture(params=[("chrome", "Gururaj"), "ff"])
def crossBrowser(request):
    return request.param
