input = eval(input("Enter a tuple: "))

string = ''.join(str(x) for x in input)
print("JOINED THE TUPLE : ",string)

reversed_tuple = input[::-1]
print("REVERSED TUPLE :",reversed_tuple)
