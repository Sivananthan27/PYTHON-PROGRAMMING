set1 = set(input("Enter the elements of the first set (space-separated): ").split())
set2 = set(input("Enter the elements of the second set (space-separated): ").split())

if set1.issubset(set2):
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")
