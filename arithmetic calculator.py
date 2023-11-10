import math
import random
print("*****ARITHMETIC CALCULATOR*****")
print("Enter your choice: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo\n6. Exponentiation")
ch=int(input("Enter your choice(1-6):\n"))
a,b=input("Enter two numbers to be operated on: ").split()
s=0.0
d=True
w='n'
while d:
    if ch==1:
        s=float(a)+float(b)
        print("Sum of the two numbers is: ",s)
        w=input("Want to do something more?(y/n)")
        if w.lower()=='y':
            ch=int(input("Enter your choice(1-6):\n"))
            a,b=input("Enter two numbers to be operated on: ").split()
        else:
            d=False
            print("*****Thanks for using*****")
    elif ch==2:
        s=float(a)-float(b)
        print("Difference of the two numbers is: ",s)
        w=input("Want to do something more?(y/n)")
        if w.lower()=='y':
            ch=int(input("Enter your choice(1-6):\n"))
            a,b=input("Enter two numbers to be operated on: ").split()
        else:
            d=False
            print("*****Thanks for using*****")
    elif ch==3:
        s=float(a)*float(b)
        print("Product of the two numbers is: ",s)
        w=input("Want to do something more?(y/n)")
        if w.lower()=='y':
            ch=int(input("Enter your choice(1-6):\n"))
            a,b=input("Enter two numbers to be operated on: ").split()
        else:
            d=False
            print("*****Thanks for using*****")
    elif ch==4:
        s=float(a)/float(b)
        print("Quotient is: ",s)
        w=input("Want to do something more?(y/n)")
        if w.lower()=='y':
            ch=int(input("Enter your choice(1-6):\n"))
            a,b=input("Enter two numbers to be operated on: ").split()
        else:
            d=False
            print("*****Thanks for using*****")
    elif ch==5:
        c=int(a)%int(b)
        print(a,"modulo",b,"= ",c)
        w=input("Want to do something more?(y/n)")
        if w.lower()=='y':
            ch=int(input("Enter your choice(1-6):\n"))
            a,b=input("Enter two numbers to be operated on: ").split()
        else:
            d=False
            print("*****Thanks for using*****")
    elif ch==6:
        c=int(a)**int(b)
        print(a, "**",b,"=",c)
        w=input("Want to do something more?(y/n)")
        if w.lower()=='y':
            ch=int(input("Enter your choice(1-6):\n"))
            a,b=input("Enter two numbers to be operated on: ").split()
        else:
            d=False
            print("*****Thanks for using*****")
    else:
        print("Wrong choice!!!\nPlease choose something within 1-6")
        ch=int(input("Enter your choice(1-6):\n"))
