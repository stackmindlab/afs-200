
# complete the following operations

# 1. Prompt the user to input a number;
# 2. Multiple this number by 3;
# 3. Add 6 to the number;
# 4. Divide the new number by 3;
# 5. Subtract the number from step 1 from the answer in step 4;
# 3. Display the results as an interger. The results should always be 2;

userNum = input("Please enter a number: ")
number = float(userNum)
magicMath = int(((number * 3  + 6) // 3) - number)
print(magicMath)

