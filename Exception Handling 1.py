def get_element_by_index(numbers, index):
    try:
        element = numbers[index]
        return element
    except IndexError:
        raise IndexError("Index is out of range")

# Prompt the user for input
numbers = input("Enter a list of numbers (space-separated): ").split()
index = int(input("Enter the index: "))

# Convert input numbers to integers
numbers = [int(num) for num in numbers]

# Get the element at the given index
try:
    result = get_element_by_index(numbers, index)
    print("Element at index", index, "is:", result)
except IndexError as e:
    print("Error:", str(e))
