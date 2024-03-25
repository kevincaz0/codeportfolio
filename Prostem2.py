def area():
	a = float(input("Enter side A: "))
	b = float(input("Enter side B: "))
	c = float(input("Enter side C: "))
	d = float(input("Enter side D: "))
	e = float(input("Enter side E: "))
	area1 = 1.0* a * b
	area2 = (a - c) * (d - e -b)
	area3 = 0.5 * (a - c) * e
	print("Room Area: " + str(area1 + area2 + area3))