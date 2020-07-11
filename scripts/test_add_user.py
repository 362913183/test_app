import sys,os,pytest,allure
sys.path.append(os.getcwd())
from Page.Page import Src_fun
from Base.Init_Driver import init_driver
from Base.read_data import read_yaml

def load_data():
    test = read_yaml('data').get('Test_data')
    key_list = []
    for i in test.keys():
        key_list.append((i, test.get(i).get('name'), test.get(i).get('phone')))
    return key_list

class Test_Add_User:
    def setup_class(self):
        self.driver = init_driver()
        self.op = Src_fun(self.driver).add_api()


    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture()
    def start_step(self):
        self.op.add_btn()

    @pytest.mark.usefixtures('start_step')
    @allure.step(title="我是步骤")
    @pytest.mark.parametrize('test_num,name,phone',load_data())
    def test_add_user(self, test_num, name ,phone):
        allure.attach('描述','描述内容')
        print('用例编号：%s' %test_num)
        self.op.input_text(name , phone)
        self.driver.get_screenshot_as_file('./screen/%s.png' %test_num)




