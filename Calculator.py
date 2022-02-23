	print("""
				_
				[/] Calcutator [\]
				[+] add || Addition
				[+] multi || Multiply 
				[+] sub || Subtract
				[+] div || Divition
				[/]------------[\]
				""")
			inok = input("Lewd@Calcualtor >> ")
			if inok == 'add':
				number_1 = int(input('Enter your first number: '))
				number_2 = int(input('Enter your second number: '))
				print('{} + {} = '.format(number_1, number_2))
				print(number_1 + number_2)
				input("Press Enter To Continue...")
				pass
			if inok == 'sub':
				number_1 = int(input('Enter your first number: '))
				number_2 = int(input('Enter your second number: '))
				print('{} - {} = '.format(number_1, number_2))
				print(number_1 - number_2)
				input("Press Enter To Continue...")
				pass
			if inok == 'multi':
				number_1 = int(input('Enter your first number: '))
				number_2 = int(input('Enter your second number: '))
				print('{} X {} = '.format(number_1, number_2))
				print(number_1 * number_2)
				input("Press Enter To Continue...")
				pass
			if inok == 'div':
				number_1 = int(input('Enter your first number: '))
				number_2 = int(input('Enter your second number: '))
				print('{} / {} = '.format(number_1, number_2))
				print(number_1 / number_2)
				input("Press Enter To Continue...")
				pass
