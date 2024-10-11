# The volume of a sphere with radius is (4/3)*pie*r**2.
#What is the volume of the sphere with radius 5.
#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places.
radius=input("Enter radius:")
print(radius)
volume_of_the_sphere=(4/3)*(22/7)*5**2
print(f"The volume of the sphere with radius 5 is {volume_of_the_sphere: .2f}")

#Create a program to calculate the area of a triangle (1/2*base*height).
#Base and height should be entered using the keyboard.

Base=input("Enter the value for base:")
Height=input("Enter the value for height:")
Base=6
Height=7
area_of_a_triangle=(1/2*Base*Height)
print(f"The area of a triangle is {area_of_a_triangle}")

#WITU has tasked you to automate a simple grading system.
#As a python student , write a program used to display the grades that the student will be receiving based on the mark scored in a subject.
# The grades are:
# 90%-100% Grade is A
# 80%-89% Grade is B
# 70%-79% Grade is C
# 60%-69% Grade is D
# 50%-59% Grade is E
# <50% Fail
marks_scored=float(input("Enter the student score in the subject (0-100):"))
#Validate the marks within a plausible range(0-100)
if 0 <= marks_scored <=100:
    if marks_scored >=90:
        grade="A"
        print("Grade", grade)
    elif marks_scored >=80:
        grade="B"
        print("Grade",grade)
    elif marks_scored >=70:
        grade="C"
        print("Grade",grade)
    elif marks_scored >=60:
        grade="D"
        print("Grade",grade)
    elif marks_scored >=50:
        grade="E"
        print("Grade",grade)
    else:
        grade="F"
        print("Grade",grade)

    




#WITU Academy is proposing a score to help students save their money .
#Design a platform that will do the following.
#Welcome to, WITI Academy Sacco.
#1 Deposit Money
#2 Withdraw money
#3 Check balance 
#Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
# If the student selects 3, the account balance should be displayed. 

Balance=0
print("Welcome to, W-+ITI Academy Sacco")
print("/nPlease choose an option:")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")
choice=input("Enter your choice (1/2/3): ")
if choice =="1":
    amount=float(input("Enter amount to deposit:"))
    if amount >=1000:
        Balance += amount
        print(f"Deposited successfully {amount}.Your new balance is {Balance}")
    else:
        print("Minimum deposit amount is 1000.")
elif choice == '2':
    amount=float(input("Enter withdraw amount:"))
    if amount >=500:
        if Balance >= amount:
            Balance-= amount
            print(f"Successfully withdrawn {amount}. Your new account balance is {Balance}. ")
        else:
            print("Insuffient balance.")
    else:
        print("Minimum withdrawal amount is 500.")
elif choice == '3': #Check Balance
    print(f"Your current balance is {Balance}.")
else:
    print("Invalid choice.")









