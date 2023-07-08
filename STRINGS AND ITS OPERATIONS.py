def is_obtained_by_deletion(str1, str2):
    first = 0
    second = 0

    while first < len(str1) and second < len(str2):
        if str1[first] == str2[second]:
            first += 1
            second += 1
        else:
            first += 1

    if second == len(str2):
        return "YES"
    else:
        return "NO"

# Example usage
string1 = "example"
string2 = "elp"
result = is_obtained_by_deletion(string1, string2)
print(result)  # Output: YES
