from ast import literal_eval
def checkType(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

n = 6

print("\n")
numList = list((num) for num in input("Please enter 5 values separated by space: ").strip().split())[:n]
print("User List: ", numList)

for i in range(0, 5):
    print(checkType(numList[i]), " ")


