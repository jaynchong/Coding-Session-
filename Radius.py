import simplegui
import random 


 def change_size(radius):
	global change_size
	change_size = radius

def change_position(position):
	global change_position
	change_position = place

def draw(canvas):
	canvas.draw_circle(radius, 20, 12, 'Green')

def button_handler():
	global button_handler
	button_handler = click


frame=simplegui.create_frame('Testing', 900, 900)
frame.set_canvas_background('Black')
button1 = frame.add_button ("Position", change_position, 100)
button2 = frame.add_button("Radius", change_size, 100)





frame.start
