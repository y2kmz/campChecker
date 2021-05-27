#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# # 第三方 SMTP 服务
mail_host = "hostname.com"  # 设置服务器
mail_user = "user@domain.net"  # 用户名
mail_pass = "password"  # 口令

sender = 'user@email.com'
receivers = ['mail_1@hotmail.com','mail_2@gmail.com','mail_3@gmail.com']  # 接收邮件

def sendMails(areaStr):

    subject = "MUJI的" + areaStr + "场地有空出来的了，赶紧去预约"

    mailText = "Hello:\r\n  MUJI的Camp场：" + areaStr +"有空出来的了，赶紧去预约。\r\n " \
               "网址：\thttp://www.muji.net/camp \r\n " \
               "Camp场：\t嬬恋キャンプ場 \r\n " \
               "区域：\t" + areaStr

    message = MIMEText(mailText, 'plain', 'utf-8')
    message['From'] = Header("camp机器人", 'utf-8')
    message['To'] = Header("你", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP(mail_host, 587)
        # smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.starttls() #SMTP server in TLS mode
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

# sendMails("Aエリア")
