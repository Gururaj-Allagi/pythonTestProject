import pytest


@pytest.mark.skip
def test_firstCode():
    print("\nguru")


@pytest.mark.smoke
def test_firstCode1():
    print("\ngururaj")
    test_firstCode()


@pytest.mark.xfail
def test_xfail(setup):
    2>3

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
