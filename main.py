from Prostem1 import silly
from Lb2 import change
from Prostem2 import area
from PassGen import passwordGenerator 
from Prostem3 import chat
from Prostem4 import divisible
from Cat import kitty
from Lb6 import year
from Lb7 import age
from Lb10 import gpaCal
from Lb9 import false
from Lb5 import digit
from Lb4 import dice
from Prostem6 import circle
from BioSheet import bio
from Lb1 import happyface
from Lb3 import speak
from Prostem8 import personal
from Pong import ping
from Prostem7 import cal
print("Welcome to my Portfolio! "+u"\U0001F638")
print("================================")
portfolio_state=True
while portfolio_state==True:
	print("Bio Page:")
	print("0. Bio Page  ")
	print("================================")
	print("Labs:")
	print("1. Lab 1 Smiley Face (Not Available Under Conditions)")
	print("2. Lab 2 Exact Change")
	print("3. Lab 3 Speaking (Not Available Under Conditions)")
	print("4. Lab 4 Dice Game")
	print("5. Lab 5 Password Generator")
	print("6. Lab 6 Leap Year")
	print("7. Lab 7 Age Related Conditions")
	print("8. Lab 8 Odd Power of Three")
	print("9. Lab 9 Input Checker")
	print("10.Lab 10 Gpa Calculator")
	print("================================")
	print("Project Stem Assignments:")
	print("P1. Project STEM Silly Sentences")
	print("P2. Project STEM Room Area")
	print("P3. Project STEM Chatbot")
	print("P4. Project STEM Divisible by 3")
	print("P6. Project STEM Animation (Not Available Under Conditions) ")
	print("P7. Project STEM Calendar ")
	print("P8. Project STEM Personal Organizer (Not Available Under Conditions)")
	print("================================")
	print("Drawings:")
	print("D1. Do Now ASCII Cat")
	print("================================")
	print("Assignments:")
	print("A1. Ping Pong Game (Not Available Under Conditions)")
	print("================================")
	lab_choice= input("Which lab do you want to see? (0/1/2/3/4/5/6/7/8/9/10/P1/P2/P3/P4/P6/P7/P8/D1/A1):")
	if lab_choice=="P1":
		silly()
	elif lab_choice=="2":
		change()
	elif lab_choice=="P2":
		area()
	elif lab_choice=="5":
		passwordGenerator()
	elif lab_choice=="P3":
		chat()
	elif lab_choice=="3":
		speak()
	elif lab_choice=="P4":
		divisible()
	elif lab_choice=="D1":
		kitty()
	elif lab_choice=="6":
		year()
	elif lab_choice=="7":
		age ()
	elif lab_choice=="8":
		false()
	elif lab_choice=="1":
		happyface()
	elif lab_choice=="9":
		digit()
	elif lab_choice=="4":
		dice()
	elif lab_choice=="0":
		bio()
	elif lab_choice=="10":
		gpaCal()
	elif lab_choice=="P6":
		circle()
	elif lab_choice=="P7":
		cal()
	elif lab_choice=="P8":
		personal()
	elif lab_choice=="A1":
		ping()
	else:
		print("Choose a Valid Lab Number")
	play_again= input("Do you want to keep exploring my portfolio? (y/n):")
	if play_again !="y":
		portfolio_state= False
print("================================")
print("Thanks for taking the time to look at my python programmimg work! If you have any feedback email me. (kcaz8210@taehs.org)")

	
		
		
	
