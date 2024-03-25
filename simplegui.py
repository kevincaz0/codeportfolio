import simpleguitk as simplegui
width=500
height=500
def draw_handler(canvas):
	canvas.draw_text("Home Page Student Profolio!",(55,150),25,"black")


                     
frame=simplegui.create_frame(":D",width,height)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()