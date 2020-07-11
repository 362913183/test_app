from selenium.webdriver.common.by import By

add_user_btn = (By.ID,'com.android.contacts:id/floating_action_button')

save_local = (By.XPATH, "//*[contains(@text,'本地')]")

input_name = (By.XPATH,'//*[contains(@text,"姓名")]')

input_phone = (By.XPATH,'//*[contains(@text,"电话")]')

# 点击返回保存按钮
click_save_back = (By.XPATH, "//*[contains(@content-desc,'向上导航')]")

# 定位用户详情页编辑按钮
usr_edit_btn = (By.ID, "com.android.contacts:id/menu_edit")


# 搜索按钮
src_btn = (By.ID,"com.android.settings:id/search")

# 文本输入框
src_text = (By.ID,"android:id/search_src_text")

#点击返回
src_back = (By.CLASS_NAME,"android.widget.ImageButton")