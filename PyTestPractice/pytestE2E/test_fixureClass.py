import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixure_demo1(self):
        print("\nfixture demo1")

    def test_fixure_dem2(self):
        print("\nfixture demo2")

    def test_fixure_demo3(self):
        print("\nfixture demo3");