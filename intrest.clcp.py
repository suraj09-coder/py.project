principle_amount=0
rate=0
time=0

while principle_amount <= 0:
    principle_amount=int(input("enter the amount :"))
    if principle_amount <= 0:
        print("the amount cannot be zero or less then zero :")


while rate <= 0:
    rate=int(input("enter the intrest rate :"))
    if rate <= 0:
        print("the rate cannot be zero or less then zero :")


while time <= 0:
    time =int(input("enter the time :"))
    if time  <= 0:
        print("the time cannot be zero or less then zero :")





total=principle_amount*pow((1+rate/100),time)
print(f"balance after {time} year is {total:.2f}$")