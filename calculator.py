# we want make calc like what want user
a=int(input('Enter Your First Number : '))
b=int(input('Enter Your Second Number : '))
res=input('Hit What You Want/ + , - , / , * ==> ')
def myCalc(a,b,res):
    if res=="+":
        # Addition
        return a+b
    elif res== "-":
         # Substraction
         return a-b
    elif res== '*':
        # Multiplication
        return a*b
    elif res == '/':
        # Handle division by zero
        if b != 0:
            return a // b
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid res!"
result=myCalc(a,b,res)
print('Your Result Is = ', result)
    
