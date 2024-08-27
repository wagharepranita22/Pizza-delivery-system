# Pizza delevery system
print("Welcome to the pizza delivery system")
size=input("Please select the size of pizza you want to order S,M or L  : ").lower()
pepperoni=input("You want some extra pepperoni for Yes press \"y\" and for no \"n\" : ").lower()
extra_chess=input("If you want extra chess if yes then \"y\" and if  no then \"N\" : ").lower()
bill=0
# code for pizza size bill calculation
if size == 's':
    bill += 15
elif size == 'm':
    bill +=20
elif size == "l" :
    bill += 25
else:
    print(f"{size} sorry this size pizza is not avilable please check some other pizza shop")

# code for pepperoni bill addition
if pepperoni=="y":
    bill += 2

# code for extra chees bill addition
if extra_chess =="y":
    bill += 1


print(f"Thank you for your order ,You have to pay  {bill} rs")