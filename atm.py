# print("SWIPE YOUR CARD")
# print("WELCOME TO UNION BANK OF INDIA")
# print("Hi,VIRESH BASAVARAH ITI")
# atm_pin=1234
# language="E or H"
# atm_pin=int(input("Enter your pin\n"))
# language=input("Select your language [E/H]\n")
# print("Choose your transcation")
# Transcation="1.Balance Enquiry  2.Cash Withdrawl\n3.Deposit\t   4.Change_pin\n5.Mobile_no\t   6.Aadhar_no"
# print(Transcation)
# while True:
# 	if atm_pin==1234:
# 		if language=="E":
# 			trans=input("")
# 			if trans=="1":
# 				slip=input("Do you want slip?\n")
# 				if slip=="yes":
# 			 		print("Take your slip\nChoose any Trancation")
# 				elif slip=="no":
# 					print("Choose any Trancation")
# 			elif trans=="2":
# 				amount=int(input("Enter your Amount\n"))
# 				if amount>=100:
# 					print("Collect your cash\nChoose any Trancation")
# 				elif amount<10000:
# 					print("Enter valid amount to proceed")
# 			elif trans=="3":
# 				Deposit=int(input("Enter your amount to deposit\n"))
# 				if Deposit>500:
# 					print("Your Amount is succesfully Deposited\nThank u for using our services")
# 				elif Deposit<"500":
# 					print("Enter valid amount to proceed")
# 				break
# 			elif trans=="4":
# 				Change_pin=int(input("Enter Here New pin number\n"))
# 				if 4==len(str(Change_pin)):
# 					print("Your pin succesfully changed")
# 				else:
# 					print("Enter valid pin to proceed")
# 			elif trans=="5":
# 				Mobile_no=int(input("Enter here Your Mobile Number\n"))
# 				if 10==len(str(Mobile_no)):
# 					print("Your Mobile number succesfully changed")
# 				else:
# 					print("It is Invalid")
# 			elif trans=="6":
# 				Aadhar_no=int(input("Enter Here Your Aadhar Number\n"))
# 				if 12==len(str(Aadhar_no)):
# 					print("Your Aadhar Number succesfully changed")
# 				else:
# 					print("It is Invalid")
# 		elif language=="H":
# 			print("Go and Learn English language")
# 	elif atm_pin!=1234:
# 		print("Wrong Pin,Try again")
