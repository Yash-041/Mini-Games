import pgzrun
from random import randint
import time

apple = Actor("apple")
score = 0
time_left = 30
game_over = False
last_update_time = time.time()

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    apple.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="black")
    screen.draw.text(f"Time: {time_left}", (700, 10), fontsize=30, color="black")

    if game_over:
        screen.draw.text("Game Over!", (350, 250), fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}", (350, 300), fontsize=30, color="red")

def on_mouse_down(pos):
    global score
    if game_over:
        return

    if apple.collidepoint(pos):
        score += 1
        place_apple()
    else:
        print("You missed!")

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def update():
    global time_left, game_over, last_update_time
    if game_over:
        return

    # Check if 1 second has passed
    current_time = time.time()
    if current_time - last_update_time >= 1:
        last_update_time = current_time
        time_left -= 1
        if time_left <= 0:
            game_over = True

pgzrun.go()
