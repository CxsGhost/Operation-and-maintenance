import smtplib
from email.mime.text import MIMEText

sent_server = smtplib.SMTP("smtp.163.com")
sent_server.login("cxsghost@163.com", "Woaiziji11")
target_email = ["akan.wt@qq.com"]
# 以下各项必须都有内容，否则会被网易退信，辣鸡
email_content = MIMEText("垃圾网易")
email_content["Subject"] = "hello,python!"
email_content["From"] = "<cxsghoat@163.com>"
email_content["To"] = target_email[0]

sent_server.sendmail("cxsghost@163.com", target_email, email_content.as_string())
sent_server.close()