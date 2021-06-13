print('-----------------WELCOME TO EVE CALCULATOR-------------------\n')
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("#-----------------COMMAND------------------------")
print("#-----------------LINE---------------------------")
print('#-----------------CALCULATOR---------------------')
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

print("---------------(+)addition--------------")
print("---------------(-)substraction----------")
print("---------------(/)for divison-----------")
print("---------------(*)multiplication------\n")

operator = input("Choose Operator: ")
if operator=='+':
    a = input("Type number: ")
    b = input("Type number: ")
    result_a = int(a) + int(b)
    print(result_a)
elif operator=='-':
    c = input("Type number: ")
    d = input("Type number: ")
    result_b = int(c) - int(d)
elif operator=='/':
    e = input("Type number: ")
    f = input("Type number: ")
    result_c = int(e) / int(f)
    print(result_c)
elif operator=='*':
    g = input("Type number: ")
    h = input("Type number: ")
    result_d = int(g)*int(h)
    print(result_d)
else:
    print("An error occured\n")

print("----------------Finish---------------------------")

