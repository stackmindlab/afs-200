#Create a variable called "applePrice" and assign it the value of fifty cents.
applePrice = 0.50

#Write the necessary code to prompt the user to enter their name.
name = input('Please enter your name: ')

#Ask the user how many apples they would like to purchase and store this value in a variable as an integer.
number = int(input(f'Hi {name}. Apples cost ${applePrice:.2f} each. How many would you like to buy? '))

#Thank the user for their purchase.  The message should contain the users name, the number of apples they purchased and the cost of each apple.
print(f'Thank you {name} for your purchase of {number} apples at a cost of ${applePrice:.2f} each.')

#this print statement is to check that number is indeed an integer and not a string 
print(type(number))