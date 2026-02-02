import random
for i in range(5):
    print("- - - - -")
colom=random.randint(0,4)
row=random.randint(0,4)
while True:
    num1=int(input("What is the colom "))
    num2=int(input("What is the row "))
    if num1==colom  and num2==row:
        print("found treasure")
        break
    if num1<colom:
        print("go right")
    if num1>colom:
        print("go left")
    if num2<row:
        print("go down")
    if num2>row:
        print("go up")
 
 