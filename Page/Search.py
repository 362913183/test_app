import Page
from Base.Base import Base


class Search(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_btn(self):
        self.click_element(Page.src_btn)

    def iput_txt(self,text):
        self.input_element(Page.src_text,text)

    def ret_btn(self):
        self.click_element(Page.src_back)
