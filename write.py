from tkinter import *
from PIL import Image, ImageDraw

canvas_width = 500
canvas_height = 500
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,128,0)
center = 250

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title( "Digit Classifier" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.configure(background='black')
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )
image1 = Image.new("RGB", (canvas_width, canvas_height), white)
draw = ImageDraw.Draw(image1)

# do the PIL image/draw (in memory) drawings
draw.line([0, canvas_width, canvas_height, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
filename = "my_drawing.jpg"
image1.save(filename)

#w.delete(ALL) # remove all items

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()