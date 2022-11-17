## In this project, you’ll create an app called Sale Price that will calculate the sale price of an item based on the item's price. 
## You will also calculate the sales tax and the total savings.

userItem = input("Please enter the product description: ")
quanity = int(float(input(f"How many of item {userItem} are being purchased? ")))
regular_price = float(input("What is the regular price? "))
TAXES = 0.065

print("Your Receipt\n------------")

if regular_price > 39.99:
    discount_price = regular_price * 0.75
elif regular_price > 19.99:
    discount_price = regular_price * 0.85
else:
    discount_price = regular_price
    
sales_tax = quanity * discount_price * TAXES
total = quanity * discount_price + sales_tax
disc_total = (regular_price - discount_price) * quanity

print(f"{quanity} {userItem} @ ${discount_price:,.2f} each")
print(f"Sales Tax ${sales_tax:,.2f}")
print(f"Total amount due ${total:,.2f}")
print(f"You saved ${(disc_total):,.2f} today.")