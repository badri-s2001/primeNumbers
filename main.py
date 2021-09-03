import time


def is_prime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False

    return True


def print_prime_numbers(a, b):
    array = []

    for i in range(a, b + 1):
        if is_prime(i):
            array.append(i)

    for num in array:
        print(num)
        time.sleep(5)


while True:
    try:
        num1 = int(input("Enter number 1: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if num1 <= 0:
            print("Enter a positive number")
        else:
            break

while True:
    try:
        num2 = int(input("Enter number 2: "))
    except ValueError as err:
        print("Please enter a number")
    else:
        if num1 <= 0:
            print("Enter a positive number")
        else:
            break

print_prime_numbers(num1, num2)
