year1=int(input("Введите год рождения первого человека"))
mon1=int(input("Введите месяц рождения первого человека"))
day1=int(input("Введите день рождения первого человека"))
year2=int(input("Введите год рождения второго человека"))
mon2=int(input("Введите месяц рождения второго человека"))
day2=int(input("Введите день рождения второго человека"))
import datetime
str1=datetime.date(year1,mon1,day1)
str2=datetime.date (year2,mon2,day2)
str3=datetime.date.today()
str4=str3-str1
str5=str3-str2
if str4>str5:
    print ("Первый человек старше")
elif str4==str5:
    print ("О динаковый возраст")
else:
    print ("Второй человек старше")
