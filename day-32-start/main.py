import smtplib
import datetime as dt
import random

MY_EMAIL = "seanhupe2024@gmail.com"
MY_PASSWORD = "heqr qcyo lqua zjqp"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()     # creates a list of all the lines in txt
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}"
        )


#gmail = smtp.gmail.com
#yahoo = smtp.mail.yahoo.com
#
# my_email = "seanhupe2024@gmail.com"
# password = "heqr qcyo lqua zjqp"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()       # secures connection to email server above
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="seanhupe@yahoo.com",
#         msg="Subject:Test Email\n\nThis is the body of the email."
#     )
#
# connection.close()



# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=1975, month=6 , day=3, hour=4)
# print(date_of_birth)

