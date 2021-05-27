# campChecker
自动监视camp场有没有空位


1，安装selenium

2，安装selenium的浏览器驱动，不同浏览器的驱动不一样

3，在checkPage.py里面设好监视网址和模拟点击的元素(文字或者id)

4，Line38其实是数文字，设置要监视的文字长什么样子

5，在sendMail.py里面设置邮件服务器，设置发件人收件人和邮件内容。SMTP端口587是需要服务器验证的，要打开TLS mode，端口25不需要。

6，在main.py里面设置你要刷几个区


