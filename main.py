import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.configure(background='grey')
canvas.pack()

def custom_init():
    canvas.create_rectangle(190,190, 210,210, fill='black')



custom_init()

canvas.mainloop()