#برنامه ای بنویسید که یک لیست از اعداد صحیح از ورودی دریافت و به صورت سعودی مرتب نماید
arr=[]
for i in range(10)
    num=int(input('enter num'))
    arr.append(num)
    
print('original list :',arr)   
for j in arr:
    for i in range(j+1, len(arr)):
         if arr[j]>= arr[x]:
             arr[j],arr[x]=arr[x],arr[j]
print('sorted list',arr)             