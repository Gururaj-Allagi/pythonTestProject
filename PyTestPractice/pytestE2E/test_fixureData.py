import pytest

from PyTestPractice.pytestE2E.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info("Gururaj")
        log.info(dataLoad[0])
        log.critical(dataLoad[1])
        print(dataLoad[0])
