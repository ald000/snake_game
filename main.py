import tkinter
import time
import random

canvas_window_size = 400    #musi byt delitelne "20"
canvas = tkinter.Canvas(width=canvas_window_size, height=canvas_window_size)
canvas.configure(background='grey')
canvas.pack()

#----setup----
def custom_init():
    global coords 
    global food_coords
    global body_coords
    global snake_head
    global score
    global start_time
    global random_x
    global random_y
    global food

    start_time = time.time()
    score = 0
    time_played = 0
    coords = [180, 180, 200, 200]
    #vytvorenie zaciatocneho bodu
    snake_head = canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='black')
    #--- vytvorenie jedla na nahodnom mieste na ploche
    random_x = 20*(random.randint(1, canvas_window_size/20))
    random_y = 20*(random.randint(1, canvas_window_size/20))
    if random_x == coords[0] and random_y == coords[1]:   #osetrenie proti zobrazeni jedla v hadovi na ziaciatku hry
        random_x = 20*(random.randint(1, canvas_window_size/20))
        random_y = 20*(random.randint(1, canvas_window_size/20))
        
    food_coords = [random_x-20, random_y-20, random_x, random_y]
    food = canvas.create_rectangle(food_coords[0], food_coords[1], food_coords[2], food_coords[3], fill='yellow', outline='yellow')

    snake_movement_south() #zacnem pohyb smerom hore

#----game over----
def game_over():
    time_played = round(time.time()-start_time, 2)  #time_played v sekundach
    print('----')
    print('koniec hry')
    print(f'skore: {score} bodov')
    print(f'odohrany cas: {time_played}s')
    print('----')

#----restart----
def restart(event):
    canvas.configure(background='grey')
    canvas.delete(snake_head)
    canvas.delete(food)
    custom_init()

#----jedlo----
def food_check():
    global food_coords
    global score
    global food
    if coords == food_coords:
        score += 1
        random_x = 20*(random.randint(1, canvas_window_size/20))
        random_y = 20*(random.randint(1, canvas_window_size/20))
        food_coords = [random_x-20, random_y-20, random_x, random_y]    #vytvori nove suradnice jedla
        canvas.coords(food, food_coords[0], food_coords[1], food_coords[2], food_coords[3])


#----pohyb----
def snake_movement_north():
    if coords[1] <= 0:
        canvas.configure(background='red')
        game_over()
    else:
        coords[1] -= 20
        coords[3] -= 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        food_check()
        canvas.after(300, snake_movement_north)

def snake_movement_south():
    if coords[3] >= canvas_window_size:
        canvas.configure(background='red')
        game_over()
    else:
        coords[1] += 20
        coords[3] += 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        food_check()
        canvas.after(300, snake_movement_south)

def snake_movement_east():
    if coords[2] >= canvas_window_size:
        canvas.configure(background='red')
        game_over()
    else:
        coords[0] += 20
        coords[2] += 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        food_check()
        canvas.after(200, snake_movement_east)

def snake_movement_west():
    if coords[2]-20 <= 0:
        canvas.configure(background='red')
        game_over()
    else:
        coords[0] -= 20
        coords[2] -= 20
        canvas.coords(snake_head, coords[0], coords[1], coords[2], coords[3])
        food_check()
        canvas.after(300, snake_movement_west)


#----ovladanie----
#canvas.bind_all('<Up>', snake_movement_north)
#canvas.bind_all('<Down>', snake_movement_south)
#canvas.bind_all('<Right>', snake_movement_east)
#canvas.bind_all('<Left>', snake_movement_west)
canvas.bind_all('w', snake_movement_north)
canvas.bind_all('s', snake_movement_south)
canvas.bind_all('d', snake_movement_east)
canvas.bind_all('a', snake_movement_west)
canvas.bind_all("r", restart)


custom_init()

canvas.mainloop()