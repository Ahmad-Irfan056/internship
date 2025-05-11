a=input("enter first number")
b=input("enter second number")
operator=input("enter operator(+-*/)")
if operator == "+":
    print(int(a)+int(b))
elif operator == "-":
        print(int(a)-int(b))
elif operator == "*":
    print(int(a)*int(b))
elif operator =="/":
     print(int(a)/int(b))
else:
     print("operator not found")
     