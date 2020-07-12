import sys,os,pytest,allure
sys.path.append(os.getcwd())

from Base.Init_Driver_To import init_driver_to
from Page.Page import Src_fun
from Base.read_data import red_data

def red_yml():
    data = red_data('search.yaml').get('SearchData')
    data_list = []
    for i in data.keys():
        data_list.append((i, data.get(i).get('test')))
    return data_list


class Test_Src:
    def setup_class(self):
        self.drvier = init_driver_to()
        self.op = Src_fun(self.drvier).src_api()
        self.op.click_btn()

    def teardown_class(self):
        self.op.ret_btn()
        self.drvier.quit()
    @allure.step('我是测试步骤001')
    @pytest.mark.parametrize("test_num, text",red_yml())
    @allure.issue('这是bug链接')
    def test_src(self, test_num, text):
        allure.attach('描述','我是测试步骤001的描述')
        self.op.iput_txt(text)
        print("用例编号：", test_num)
        self.drvier.get_screenshot_as_file('./screen/%s.png' %test_num)
