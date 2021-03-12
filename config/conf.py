import os
from selenium.webdriver.common.by import By
from tools.times import datetime_strftime


class ConfigManager(object):
    # 当前项目顶层目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 配置文件
    INI_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 日志目录
    LOG_PATH = os.path.join(BASE_DIR, 'logs')

    # 报告目录
    REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': 'sunkl@olymtech.com',
        'password': 'Test0313',
        'smtp_host': 'smtp.exmail.qq.com',
        'smtp_port': 465

    }

    # 邮件收件人
    ADDRESSEE = [
        '446874146@qq.com'
    ]

    @property
    def screen_path(self):
        """截图目录"""
        screenshot_dir = os.path.join(self.BASE_DIR, 'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        now_time = datetime_strftime
        screen_file = os.path.join(screenshot_dir, "{}.png".format(now_time))
        return now_time, screen_file


cm = ConfigManager()

if __name__ == '__main__':
    # print(BASE_DIR)
    print(cm.BASE_DIR)
    print(cm.INI_PATH)
    print(os.path.abspath(__file__))