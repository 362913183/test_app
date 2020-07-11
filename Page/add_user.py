from Base.Base import Base
import Page

class Add_User(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def add_btn(self):
        self.click_element(Page.add_user_btn)

    def save_loc(self):
        self.click_element(Page.save_local)

    def input_text(self, name, phone):
        self.input_element(Page.input_name, name)
        self.input_element(Page.input_phone, phone)
        self.click_element(Page.click_save_back)
        if self.if_element(Page.usr_edit_btn):
            self.driver.keyevent(4)


