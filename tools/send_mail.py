#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import zmail
from config.conf import cm

REPORT_PATH = cm.REPORT_PATH
EMAIL_INFO = cm.EMAIL_INFO
ADDRESSEE = cm.ADDRESSEE


def send_report():
    """发送报告"""
    with open(REPORT_PATH, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': '446874146@qq.com',
            'subject': '最新的测试报告邮件',
            'content_html': content_html,
            'attachments': [REPORT_PATH, ]
        }
        server = zmail.server(*EMAIL_INFO.values())
        server.send_mail(ADDRESSEE, mail)
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))
    else:
        print("测试邮件发送成功！")


if __name__ == "__main__":
    '''请先在config/conf.py文件设置QQ邮箱的账号和密码'''
    send_report()