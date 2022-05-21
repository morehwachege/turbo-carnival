def add(val1, val2):
        return val1 + val2

def subtract(val1, val2):
    return val1 - val2

def division(val1, val2):
    return val1 / val2

def multiplication(val1, val2):
    return val1 * val2

def modulus(val1, val2):
    return val1 % val2

def get_input():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    return num1, num2


print("""
Please Enter operation
1: Addition \n
2. Division \n
3. Multiplication \n
4. Subtraction \n
5. Modulus
""")
choice = int(input("Choice = "))
nums = get_input()
if choice == 1:
    print("Answer is: ", add(nums[0], nums[1]))
if choice == 2:
    print("Answer is: ", division(nums[0], nums[1]))
if choice == 3:
    print("Answer is: ", multiplication(nums[0], nums[1]))
if choice == 4:
    print("Answer is: ", subtract(nums[0], nums[1]))
if choice == 5:
    print("Answer is: ", modulus(nums[0], nums[1]))
