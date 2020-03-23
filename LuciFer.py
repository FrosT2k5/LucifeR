print("Welcome to TerMiNaL-LuCiFeR BY FrosT & DarK\nEnter the following commands for functions\nfollowing functions are available\nC-calculator\nL-Loop print\nT-Tables\nD-dictionary\n")
cndn = input("Enter the command: ")

if cndn == 'C':
	a = input("Enter 1st number: ")
	b = input("Enter 2nd number: ")
	op = input("Enter the operation (+,-,*,/): ")

	if op == '+':
		c=int(a)+int(b)
		print("Addition:",c,)
	
	elif op == '-':
		c=int(a)-int(b)
		print("Subtraction:",c,)
	
	elif op == '*':
		c=int(a)*int(b)
		print("Multiplication:",c,)
	
	elif op == '/':
		c=int(b)/int(a)
		print("Division:",c,)
	
	else:
		print('Please enter one of these (+,-,*,/)')
	print('\nThanks for using terminal LucifeR')		

elif cndn == 'L':
	lp = input('Enter the sentence to be looped: ')
	no = input('Enter the number of times to be printed: ')	
	i=1
	while (i<=int(no)):
		print(lp)
		i += 1
	print('\nThanks for using terminal LucifeR')

elif cndn == 'T':
	ta = input('Enter the number for its table: ')
	ml = input('Enter the number of times till which you want it\'s table: ')
	j = 1
	while (j<=int(ml)):
		ft=int(ta)*int(j)
		print(ta,'x',j,'=',ft)
		j += 1
	print('Thanks for using terminal LucifeR')

elif cndn == 'D':
	print('Enter the word for it\'s meaning following words are available:\nfragments\nmodestly\ngrunting\nepitome\npotent\ncommending\nlegs\ntreble\ngrimly\nunhindered')
	print("More words will be added soon :)")
	wd = input("Enter one of the word from above to get its meaning: ")
	if wd == 'fragments':
		print('Fragments-Tiny Pieces')
	elif wd == 'modestly':
		print("Modestly-Without boasting,in a humble way")
	elif wd == 'grunting':
		print("grunting-making low guttural sounds")
	elif wd == 'epitome':
		print("Epitome-A perfect example")
	elif wd == 'potent':
		print("Potent-Powerful and Effective")
	elif wd == 'commending':		
		print("Commending-Official Praising")
	elif wd == 'legs':			
		print("Legs-knee to ankle")
	elif wd == 'treble':
		print("Treble-Three times weaker than")
	elif wd == 'grimly':
		print("Grimly-Seriously")
	elif wd == 'unhindered':
		print("Unhindered-Without any disturbances")
	else:
		print("Please enter the words which are available and enter them in lower case only")
	print('Thanks for using terminal LucifeR')
	
else:
	print('Please use the options that are provided:')
	print('Thanks for using terminal LucifeR')
		


