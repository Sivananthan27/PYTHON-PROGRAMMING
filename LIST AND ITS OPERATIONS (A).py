numbers = []
n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    num = int(input(f"Enter the value - {i+1}: "))
    numbers.append(num)

search_num = int(input("Enter the element to be found: "))

positive_indices = []
negative_indices = []

occurrences = numbers.count(search_num)

if occurrences > 0:
    for i in range(len(numbers)):
        if numbers[i] == search_num:
            positive_indices.append(i+1)
            negative_indices.append(-(len(numbers)-i))
    
    print(f"Element {search_num} occurs {occurrences} times in the list.")
    print("Positive Index:", ', '.join(map(str, positive_indices)))
    print("Negative Index:", ', '.join(map(str, negative_indices)))
else:
    print(f"Element {search_num} is not present in the list.")
