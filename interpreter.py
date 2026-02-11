expression = input("Expression: ")
if expression[2] == "+":
    result = int(expression[0]) + int(expression[4])    
elif expression[2] == "-":
    result = int(expression[0]) - int(expression[4])
elif expression[2] == "*":
    result = int(expression[0]) * int(expression[4])    
elif expression[2] == "/":
    result = int(expression[0]) / int(expression[4])       
print(f"{round(result, 1)}")