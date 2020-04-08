
import sys
def banner ():
    ban = """
     _                _  __     _____  
    | |              (_)/ _|   |  __ \ 
    | |    _   _  ___ _| |_ ___| |__) |
    | |   | | | |/ __| |  _/ _ \  _  / 
    | |___| |_| | (__| | ||  __/ | \ \ 
    |______\__,_|\___|_|_| \___|_|  \_\\
    """
    
    print(ban)
    print('Welcome to Terminal LucifeR by FrosT,LemoN,Yuvi and DarK.Enter help or h for list of options')
    
    
def nth():
    z = open('files/holp.txt')
    ct = z.read()
    print(z)
    z.close()
  

def help():
    file = open('files/help.txt')
    cont = file.read()
    print(cont)
    file.close()
 
def calc():
    print('Enter 1 for addition/subtraction/multiplication/division')
    print('Enter 2 for square,cube,square root and raise power')
    ip = int(input('Choose option 1 or 2: '))
    if ip == 1:
        num1 = float(input('Enter first number: '))
        op = input('Enter operation: ')
        num2 = float(input('Enter second number: '))
        
        if op == '+':
            print('Addition: ',num1+num2)
        elif op == '-':
            print('Subtraction: ',num1-num2)
        elif op == '*':
            print('Multiplication: ',num1*num2)
        elif op == '/':
            print('Division: ',num1/num2)
        else:
            print('Please enter one of these: +,-,* or /')
   
            
    elif  ip == 'options':
            nth()
           
    elif  ip == 2:
        while True:
            print('Enter square, cube, squareroot or sqrt, raise or raiseto')
            lo = input('Calc: ')
            if lo == 'square':
                sq = int(input('Enter number for it\'s square: '))
                print('Square: ',sq**2 )
            elif lo == 'cube':
                cb = int(input('Enter number for it\'s cube: '))
                print('Cube: ',cb**3)
            elif lo == 'squareroot' or lo == 'square root' or lo == 'sqrt':
                sr = float(input('Enter number for its square root: '))
            elif lo == 'quit' or 'exit':
                sys.exit()
                print('The square root of the number is: ',sr**(1/2))                
            elif lo == 'raiseto' or lo == 'raise' or lo == 'power':
                nm = int(input('Enter a number to raise it\'s power: '))
                pr = int(input('Enter the index number: '))
                print('The result is: ',nm**pr)
               
            else:
                print('Incorrect option,enter options for getting list of options')
               
    else:
        print('Please enter option 1 or 2')
        
                
                
def lp():
    st = input('Enter the sentence to be looped: ')
    no = input('Enter the number of times to be printed: ')
    i = 1
    while(i<=int(no)):
        print(st)
        i += 1
        

def tables():
    ta = int(input('Enter the number for its table: '))
    bl = int(input("Enter the number of times till you want it's table: "))
    j = 1
    while(j<=bl):
         print(ta,'x',j,'=',ta*j)
         j += 1
        

def numgame():
    fun = float(input('Enter any number for its weight on other planets: '))
    print("If your weight was",fun,"kgs on earth ,then your weight on :-\nMercury =",fun*0.38,'\nVenus =',fun*0.9,'\nMars =',fun*0.38,'\nJupiter =',fun*2.34,'\nSaturn =',fun*1.06,'\nUranus =',fun*0.91,'\nNeptune =',fun*1.19,'\nPluto',fun*0.06)    
  
banner()
while True:

    inp = str(input('LucifeR: '))
    
    if inp == 'calc' or inp == 'calculator':
        calc()
    elif inp == 'help' or inp == 'h':
        help()
    elif inp == 'lp' or inp == 'loopprint':
        lp()
    elif inp == 'numbergame' or inp == 'weight':
        numgame()
    elif inp == 'tables':
        tables()
    elif inp == 'quit' or inp == 'exit':
        sys.exit()
    else:
        print('Please enter one of the following options:')
        help()





                               

