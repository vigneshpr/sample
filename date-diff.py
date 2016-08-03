from datetime import date

date1 = date(1993, 5, 26)
import datetime


#date2 = date(2014, 7, 11)

diff =  datetime.date.today() - 	date1
print(diff.days)
