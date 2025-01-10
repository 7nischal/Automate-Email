import smtplib

my_email ="testpython611@gmail.com"
password ="TestPtython"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email, to_addrs="adhikari.nischal2011@gmail.com", msg="Hello")
connection.close()