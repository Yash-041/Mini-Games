import pgzrun
from random import randint

ICON = "C:/Users/yashs/OneDrive/Desktop/dogo.webp"
TITLE = "Coin Collector"
WIDTH = 500
HEIGHT = 500
score = 0
game_over = False
countdown = 30

dog = Actor("dog")
dog.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    dog.draw()
    coin.draw()
    
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    
    if not game_over:
        screen.draw.text(f"Time Left: {countdown}s", color="black", topright=(WIDTH - 10, 10))
    
    if game_over:
        screen.fill("Black")
        screen.draw.text("Final Score: " + str(score), color="Red", center=(WIDTH / 2, HEIGHT / 2), fontsize=60)

def place_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)

def countdown_tick():
    global countdown, game_over
    countdown -= 1
    if countdown <= 0:
        game_over = True

def update():
    global score

    if game_over:
        return

    if keyboard.left: dog.x -= 2
    if keyboard.right: dog.x += 2
    if keyboard.up: dog.y -= 2
    if keyboard.down: dog.y += 2

    if dog.colliderect(coin):
        score += 10
        place_coin()

clock.schedule_interval(countdown_tick, 1.0)

place_coin()

pgzrun.go()
