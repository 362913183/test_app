from Page.Search import Search
from Page.add_user import Add_User


class Src_fun:
    def __init__(self,driver):
        self.driver = driver

    def src_api(self):
        return Search(self.driver)

    def add_api(self):
        return Add_User(self.driver)
