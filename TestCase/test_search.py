#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import time
import allure
import pytest
from tools.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


@allure.feature("测试百度模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self, drivers):
        """打开百度"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    @allure.story("搜索selenium结果用例")
    def test_001(self, drivers):
        """搜索"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        time.sleep(9)
        assert result

    @allure.story("测试搜索候选用例")
    def test_002(self, drivers):
        """测试搜索候选"""
        search = SearchPage(drivers)
        search.input_search("selenium")
        log.info(list(search.imagine))
        assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    # pytest.main(['test_search.py'])
    pytest.main(['test_search.py', '--alluredir', './allure'])
    os.system('allure serve allure')