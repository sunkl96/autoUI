import os
import configparser
from config.conf import cm

HOST = 'HOST'
INI_PATH = cm.INI_PATH


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件%s不存在!" % INI_PATH)
        self.config = configparser.RawConfigParser()    # 当有%的符号时请使用Raw读取
        self.config.read(INI_PATH, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
    print(INI_PATH)
