def factorial(n):
   if n == 0 or n == 1:
        return 1
   else:
        return n * factorial(n-1)

def is_palindrome(n):
    num = str(n)
    return num == num[::-1]

def count_digits(n):
    return len(str(number))
number = int(input("Enter an integer: "))

if number % 2 == 1:  # Odd number
        fact = factorial(number)
        digit_count = count_digits(fact)
        print(f"The factorial of {number} is: {fact}")
        print(f"The number of digits in the factorial is: {digit_count}")
else:  # Even number
    if is_palindrome(number):
            print(f"{number} is a palindrome.")
    else:
            print(f"{number} is not a palindrome.")

    

