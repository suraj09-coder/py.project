foods=[]
prices=[]
total=0

while True:
    food=input("enter the food you want /if you want to quite prees(q)   :")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"enter the price of the {food} :"))
        foods.append(food)
        prices.append(price)

print("your order is")

for food in foods:
    print(food,end=" ")

for price in prices:
    total=total+price
print()   
print(f"you have to pay{total}")

