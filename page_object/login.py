from page.webpage import WebPage,sleep
from common.readelement import Element

login = Element('login')


class Login(WebPage):
    """
    登录类
    """

    def input_username(self,context):
        self.input_text(login['用户名输入框'], txt=context)

    def input_password(self,context):
        self.input_text(login['密码输入框'], txt=context)

    def click_login(self):
        self.is_click(login['登录按钮'])