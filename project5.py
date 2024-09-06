str1 = int( input( "Введите трехзначное число"))
if 100<=str1<1000:
    str2= int(str (str1) [0]) + int( str (str1) [1]) + int(str (str1) [2])
    print (str2)
    str3= int(str (str1) [0]) * int(str (str1) [1]) * int( str (str1) [2])
    print(str3)
    pass

else:
    print ("число не трехзначное")