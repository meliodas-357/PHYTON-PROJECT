def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def mutiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)

def claculator():
    print('simple claculator')
    print('enter the choice ')
    print('1- addition')
    print('2- subtraction')
    print('3- multiplication')
    print('4- dividing')
    print('5- exit')
    
    while True:
        choice= input("enter your choice")
        
        if choice == '5':
            print("thanks for using our code")
            break
            
        elif choice in ('1','2','3','4','5'):
            try:
                num1=int(input('enter the nummber1'))
                num2=int(input('enter the nummber2'))
                
                if choice=='1':
                  print(f"{num1}+{num2}={add(num1,num2)}")
                  
                if choice=='2':
                  print(f"{num1}-{num2}={subtract(num1,num2)}")
                  
                if choice=='3':
                  print(f"{num1}*{num2}={mutiply(num1,num2)}")
                  
                if choice=='4':
                  print(f"{num1}/{num2}={divide(num1,num2)}")
                  
            except ValueError:
                print('enter numeric data')
                
        else:
                print('invalid choice, enter the option again')
                
claculator()
                  
                  
                  
                  
                  