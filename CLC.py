num1=float(input("enter a number :"))
num2=float(input("enter a number :"))

result=input("enter the operation,for add(+),for subtraction(-),for multiply(*),for divide(/)  :")
if result=="+":
    result=num1+num2
    print(round(result))
elif result=="-":
    result=num1-num2
    print(result)

elif result=="*":
    result=num1*num2
    print(result)

elif result=="/":
    result=num1/num2
    print(result)   

else:
    print("ERROR")    