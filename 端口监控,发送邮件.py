#/usr/bin/python3
#-*- coding:utf-8 -*-
from requests_html import HTMLSession
import smtplib
from email.mime.text import MIMEText

Session = HTMLSession()
my=open(r'C:\Users\azhe\Desktop\url.txt')
for x in my:
    sender = 'zhe.wang@shtongzhu.com.cn'  # 发件人
    password = 'Tz123456'  # 发件人密码
    receiver = ['zhe.wang@shtongzhu.com.cn'] # 收件人邮箱
    subject = 'python测试'  # 邮件主题
    content = '端口异常'  # 邮件内容
    msg = MIMEText(content+x, 'plain', 'utf-8')
    msg['subject'] = subject
    msg['from'] = sender
    for h in receiver:
        msg['TO'] =h
    x = x.strip()
    url=x
    r = Session.get(url)
    rest = r.html.find('h1')
    if rest[0].text != 'hello world':
        try:
            smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', '465')
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            print('发送成功')
        except Exception:
            print("发送失败")
    else:
        print('端口正常')
my.close()

# sender = 'zhe.wang@shtongzhu.com.cn'  # 发件人
# password = 'Tz123456'  # 发件人密码
# receiver = '1352010395@qq.com'  # 收件人邮箱
# subject = 'python测试'  # 邮件主题
# content = '端口异常'  # 邮件内容
# msg = MIMEText(content, 'plain', 'utf-8')     #添加邮件内容到msg
# msg['subject'] = subject                      #添加邮件主题到msg
# msg['from'] = sender                          #添加发件人账号到msg
# msg['TO'] = receiver                          #添加收件人账号到msg


