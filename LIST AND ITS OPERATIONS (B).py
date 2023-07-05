numbers = []
n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    num = int(input(f"Enter the value - {i+1}: "))
    numbers.append(num)

ascending = True

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
        ascending = False
        break

if ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
