def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("please select operator-\n " \
"1. add\n" \
"2.sub\n" \
"3.multiplication\n" \
"4.division\n" )
select=int(input("select operations from 1,2,3,4 :"))
num_1=int(input("enter first number:"))
num_2=int(input("enter second number :"))
if select==1:
    print(num_1,"+"num_2,"=",add(num_1,num_2))
elif select==2:
    print(num_1,"-"num_2,"=",subtract(num_1,num_2))
elif select==3:
    print(num_1,"*"num_2,"=",multiplication(num_1,num_2))
elif select==4:
    print(num_1,"/"num_2,"=",divide(num_1,num_2))
else:
    print("invalid input")