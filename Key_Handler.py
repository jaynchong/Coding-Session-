import simplegui 
screensaver_text="Khoa still didn't do his homework"

def draw_handler(canvas):
    canvas.draw_text(screensaver_text, (20, 20), 12, 'White')

def input_handler(text_input):
    global screensaver_text
    screensaver_text = text_input
    
def keydown_handler(key):
    global screensaver_text
    if (key == simplegui.KEY_MAP['space']):
        screensaver_text = ""
    elif(key == simplegui.KEY_MAP['w']):
        screensaver_text = "up"
    elif(key == simplegui.KEY_MAP['a']):
        screensaver_text ="left"
    elif(key == simplegui.KEY_MAP['d']):
        screensaver_text = "right"
    elif(key == simplegui.KEY_MAP['s']):
        screensaver_text = "down"
    
    
    
frame = simplegui.create_frame('Anything',400,400)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
inp =frame.add_input('My label', input_handler, 50)

frame.start()