def get_number():
    contChecking = True

    while contChecking:
        custNum = input('Please enter a positive number: ')

        if custNum.isdigit():
            countDown(int(custNum)+1)
            contChecking = False
        else:
            print('Invalid input. Please enter a positive number:')

def countDown(numeral):
    for even in range(numeral):
        if even % 2 == 0:
            print(even)

get_number()