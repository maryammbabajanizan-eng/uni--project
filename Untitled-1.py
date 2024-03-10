#برنامه ای بنویسید که لیست اعداد زوج را در دو خط کد به ما نشان 
#numbers=[i for i in range(0,101) if i/2 == 0 if i>20 if i<40]
#print(numbers)

#برنامه ای بنویسید وزن یک مولکول اب ) 10*3 به توان 23-و وزن اب در حدود 950 گرم است برنامه ای بنویسید که  وزن اب را   بر حسب لیتر از ورودی خوانده و تعداد مولکوا های ان را محاسبه کند 
#3.0e-23
#w=int(input("w ="))
#m=3.0e-23
#liter=950
#tedad=(w*liter)/m
#print(tedad)

#برنامه ای بنویسد که یک عدد از ورودی بگیره و تشخصی دهد که ایا ان عدد کامل است یا خیر
number=int(input("enter a number ="))
sum=0
for i in range(1,number):
    if(number % i ==0):
      sumlist.append(i)
      sum=sum+i
if(sum == number):
    print("kamel ast")   
    print(sumlist)
else:
    print("nist")  
    print(sumlist)  