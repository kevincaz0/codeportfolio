def circle():
	import simplegui
	import random
	x=-50
	def draw_handler(canvas):
	    global x
	    x=x+2
	    canvas.draw_circle((600,0),100,2,"#FFF68F","#FFFF00")
	    canvas.draw_line((430,10),(480,10),10,"#FFFF00")
	    canvas.draw_line((500,65),(450,80),10,"#FFFF00")
	    canvas.draw_line((540,110),(500,150),10,"#FFFF00")
	    canvas.draw_line((590,120),(590,170),10,"#FFFF00")
	
	    canvas.draw_circle((550,550),300,2,"red","red")
	    canvas.draw_circle((550,550),250,2,"orange","orange")
	    canvas.draw_circle((550,550),200,2,"yellow","yellow")
	    canvas.draw_circle((550,550),150,2,"green","green")
	    canvas.draw_circle((550,550),100,2,"blue","blue")
	    canvas.draw_circle((550,550),50,2,"purple","purple")
	    canvas.draw_circle((550,570),35,2,"#63B8FF","#63B8FF")
	    canvas.draw_circle((x,100),50,2,"white","white")
	    canvas.draw_circle((x+50,120),50,2,"white","white")
	    canvas.draw_circle((x-50,120),50,2,"white","white")
	    canvas.draw_circle((x-10,120),30,2,"white","white")
	    canvas.draw_circle((x+30,100),20,2,"white","white")
	    canvas.draw_circle((x,120),50,2,"white","white")
	    canvas.draw_circle((x+90,140),30,2,"white","white")
	    canvas.draw_circle((x-90,140),30,2,"white","white")
	    canvas.draw_circle((x+150,300),50,2,"white","white")
	    canvas.draw_circle((x+200,320),50,2,"white","white")
	    canvas.draw_circle((x+190,320),50,2,"white","white")
	    canvas.draw_circle((x+140,320),30,2,"white","white")
	    canvas.draw_circle((x+120,300),20,2,"white","white")
	    canvas.draw_circle((x+150,320),50,2,"white","white")
	    canvas.draw_circle((x+240,340),30,2,"white","white")
	    canvas.draw_circle((x+100,340),30,2,"white","white")
	    canvas.draw_circle((x+470,180),50,2,"white","white")
	    canvas.draw_circle((x+520,200),50,2,"white","white")
	    canvas.draw_circle((x+420,200),50,2,"white","white")
	    canvas.draw_circle((x+460,200),30,2,"white","white")
	    canvas.draw_circle((x+500,180),20,2,"white","white")
	    canvas.draw_circle((x+470,200),50,2,"white","white")
	    canvas.draw_circle((x+560,220),30,2,"white","white")
	    canvas.draw_circle((x+380,220),30,2,"white","white")
	    canvas.draw_polygon([(0,580),(600,580),(600,600),(0,600)],2,"#98FB98","#98FB98")
	        #hi
	    
	    if x >650:
	        x=-50
	    for r in range(4):
	        print(" ")
	frame = simplegui.create_frame('Testing', 600, 600)
	frame.set_canvas_background("#63B8FF")
	frame.set_draw_handler(draw_handler)
	frame.start()
	