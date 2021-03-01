import tkinter
import time

canvas_window_size = 400

canvas = tkinter.Canvas(width=canvas_window_size, height=canvas_window_size)
canvas.configure(background='grey')
canvas.pack()

#----initialization----
def custom_init():
    global coords 
    global snake_head
    global score
    global start_time

    start_time = time.time()
    score = 0
    time_played = 0
    coords = [180, 180, 200, 200]
    snake_head = canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='black') #vytvorim zaciatocny bod
    snake_movement_north() #zacnem pohyb

#----game over----
def game_over():
    time_played = round(time.time()-start_time, 2)  #time_played v sekundach
    print('koniec hry')
    print(f'skore: {score} bodov')
    print(f'odohrany cas: {time_played}s')

#----restart----
def restart(event):
    canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='grey', outline='grey')
    canvas.configure(background='grey')
    custom_init()

#----movement----
def snake_movement_north():
    if coords[1]-20 <= 0:
        canvas.configure(background='red')
        game_over()
    else:
        coords[1] -= 20
        coords[3] -= 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        canvas.after(300, snake_movement_north)

def snake_movement_south():
    pass

def snake_movement_east():
    if coords[2] >= canvas_window_size:
        canvas.configure(background='red')
        game_over()
    else:
        coords[0] += 20
        coords[2] += 20
        print(coords)
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        canvas.after(200, snake_movement_east)

def snake_movement_west():
    pass


#----controls----
#canvas.bind('<Up>', snake_movement_north)
#canvas.bind('<Down>', snake_movement_south)
#canvas.bind('<Right>', snake_movement_east)
#anvas.bind('<Left>', snake_movement_west)
#canvas.bind_all('w', snake_movement_north)
#canvas.bind_all('s', snake_movement_south)
#canvas.bind_all('d', snake_movement_east)
#canvas.bind_all('a', snake_movement_west)
#canvas.bind_all("r", restart)


custom_init()

canvas.mainloop()