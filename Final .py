def calr(l,m,n): 
    if n == '+':                     #sum
        print("\n",a,"+",b,"=",a+b)
    elif n == '-':                   #difference
        print("\n",a,"-",b,"=",a-b) 
    elif n == '*':                   #multiplication 
        print("\n",a,"*",b,"=",a*b)
    elif n == '/':                   #division     
        print("\n",a,"/",b,"=",float(a/b))
    else:
        print("Some error occured,Try again")
        
def oddeven(c):
    if c%2==0:
        print("even")
    else: 
        print("odd")
        
def factorial(c):
    fac=1
    for i in range(1,c+1):
        fac=fac*i
    print(fac)
        
def arm(c):
    strnum=str(c)
    sum=0
    for i in strnum:
        sum=sum+int(i)**3
    if c == sum:
        print(c,"is an armstrong number")
    else:
        print(c,"is not an armstrong number")

def prime(c):
    if c !=0:
        count=0
        for i in range(1,c+1):
            if c%i==0:
                count+=1
    #print(count)
        if count<=2:
            print("The number",c,"is prime")
        else:
            print(c,"is not a prime")
    else:
        print("0 is not a prime")
    
                
# main program    
print("""Select your choice:
For Binary Calculations--Enter 1
For Number Functions--Enter 2
""")
x=int(input("Your Choice:"))
# binary calculator 
if x==1:
    print("""
    Binary Calculator
    :::::::::::::::::
    """)
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:")) 
    print("""
For addition→ Enter +
For subtraction→ Enter -
For multiplication→ Enter *
For division→ Enter /
    """)
    o = input("Enter operation:") #opertion
    calr(a,b,o)                   #function calling
if x==2:
    print("""
    Number Functions
    ::::::::::::::::
    """)
    c=int(input("Enter the number:"))
    print("""
For checking : prime     → Enter 1
               odd even  → Enter 2 
               armstrong → Enter 3
               factorial → Enter 4
""") 
    y=int(input("Enter your choice:"))
    if y == 1:
        prime(c)
    elif y == 2:
        oddeven(c)
    elif y == 3:
        arm(c)
    elif y == 4:
        factorial(c)
    else :
        print("Some error occured,Try again")
else:
    print("Some erroe occured,Try again")






