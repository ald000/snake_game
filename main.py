import tkinter

canvas = tkinter.Canvas(width=400, height=400)
canvas.configure(background='grey')
canvas.pack()

#----initialization----
def custom_init():
    global coords 
    global snake_head
    global score

    coords = [190, 190, 210, 210]
    snake_head = canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='black') #vytvorim zaciatocny bod
    snake_movement_north()

#----game over----
def game_over():
    print('game over')
    print(f'skore:', score)
    print(f'time_played:', time_played)

#----movement----
def snake_movement_north():
    if coords[1]-20 == 0 and coords[3]-20 == 0:
        canvas.configure(background='red')
        game_over()
    else:
        coords[1] -= 20
        coords[3] -= 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        canvas.after(200, snake_movement_north)

def snake_movement_east():
    if coords[1]-20 == 0 and coords[3]-20 == 0:
        canvas.configure(background='red')
        game_over()
    else:
        coords[1] -= 20
        coords[3] -= 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        canvas.after(200, snake_movement_east)




custom_init()

canvas.mainloop()