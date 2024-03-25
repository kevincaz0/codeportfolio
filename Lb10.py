def gpaCal():
	subjects=[]
	grade=[]
	def gpaCalculator():
	    name=input("What's your name? ")
	    numS=int(input("How many subjects do you take? "))
	    for i in range(numS):
	        subjects.append(input("What subject are you taking? "))
	        grade.append(int(input("What's your grade for the class? ")))
	    print("Nice to meet you "+name+"!!")
	    gpa=0
	    for i in range(len(subjects)):
	        print(subjects[i], ":", grade[i])
	        gpa=gpa+grade[i]
	    finalgpa=gpa/len(subjects)
	    print("So, your total GPA is: ", finalgpa)
	gpaCalculator()