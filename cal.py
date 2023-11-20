import math
def add():
    result=0
    while True:
        a=(input('Enter number to add or enter Q to quit and get result'))
        if a=="Q":
            return result
        else:
            result+=int(a)
    return result
def sub():
    first_num=(input("Enter first number"))
    result=int(first_num)
    while True:
        a=(input('Enter number to add or enter Q to quit and get result'))
        if a=="Q":
            return result
        else:
            result-=int(a)
    return result
def mul():
    first_num=(input("Enter first number"))
    result=int(first_num)
    while True:
        a=(input('Enter number to add or enter Q to quit and get result'))
        if a=="Q":
            return result
        else:
            result*=int(a)
    return result

def div():
    result=0
    a=int(input('Enter qoutient'))
    b=int(input('enter divisor'))
    result=a/b
    return result
def modolus():
    result=0
    a=int(input('Enter qoutient'))
    b=int(input('enter divisor'))
    result=a%b
    return result
def sqrtt():
    a=int(input("enter your number for sqrt"))
    result=math.sqrt(a)
    print(result)

while True:
    print("*********************")
    print('1 to do add')
    print('2 to do subtract')
    print('3 to do multiply')
    print('4 to do div')
    print('5 to do modulous')
    print('6 to do square root')
    print('7 to exit')
    print("*********************")
    choice=int(input('enter choice what you want to do'))
    if choice ==1:
        print("*********************")
        print("result",add())
        print("*********************")
    elif choice == 2:
        print("*********************")
        print("result",sub())
        print("*********************")
    elif choice==3:
        print("*********************")
        print("result",mul())
        print("*********************")
    elif choice==4:
        print("*********************")
        print("result",div())
        print("*********************")
    elif choice==5:
        print("*********************")
        print("result",modolus())
        print("*********************")
    elif choice==5:
        print("*********************")
        print("result",sqrtt())
        print("*********************")
    
    elif choice==7:
        break
    else:
        print("*********************")
        print('enter valid number')
        print("*********************")
