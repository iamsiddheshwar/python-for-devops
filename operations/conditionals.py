
num1 =int (input("enter first number:"))
num2 =int (input("enter second number:"))

choice=input("Enter your choice: (Operation : +,-,*,/,% ) : ")

if choice=="+":
    sum_of_num=num1+num2
    print("Addition:", sum_of_num)

elif choice=="-":
    diff_of_num=num1-num2
    print("Differance:", diff_of_num)

elif choice=="*":
    prod_of_num=num1*num2
    print("Multiplication:",prod_of_num)

elif choice=="/":
    div_of_num=num1/num2
    print("Division:",div_of_num)

elif choice=="%":
    rem_of_num=num1%num2
    print("Reminder:",rem_of_num)

else:
    print("Invalid Choice")
     