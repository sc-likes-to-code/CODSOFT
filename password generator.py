import string
import random

print("**********Password Generator**********")

l = int(input("Enter desired length of password: "))
print('''\nChoose character set for password from these or choose to exit by entering '4' : \n1. Letters\n2. Digits\n3. Special characters\n4. Exit\n''')

cl = ""

while(True):
    c = int(input("Pick a number: "))
    
    if(c == 1):
        cl += string.ascii_letters
    elif(c == 2):
        cl += string.digits
    elif(c == 3):
        cl += string.punctuation
    elif(c == 4):
        break
    else:
        print("Please pick a valid option!")

p = []

for i in range(l):
    randomchar = random.choice(cl)
    p.append(randomchar)

print("The random password is " + "".join(p))
