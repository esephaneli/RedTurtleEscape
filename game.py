import turtle
import random
import math
import time

# Ekran ayarları
screen = turtle.Screen()
screen.title("Kaplumbağa Yakalama Oyunu")
screen.bgcolor("lightblue")
screen.setup(800, 600)

# Oyuncu kaplumbağası
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Hedef kaplumbağa
target = turtle.Turtle()
target.shape("turtle")
target.color("red")
target.penup()
target.speed(0)

# Skor yazısı
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.color("black")

# Süre yazısı
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(0, 230)
time_display.color("black")

# Oyun değişkenleri
score = 0
game_time = 30
start_time = time.time()
game_active = True


def move_target():
    """Hedef kaplumbağayı rastgele bir konuma taşır"""
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    target.goto(x, y)


def move_up():
    """Oyuncuyu yukarı hareket ettirir"""
    y = player.ycor()
    if y < 280:
        player.sety(y + 20)


def move_down():
    """Oyuncuyu aşağı hareket ettirir"""
    y = player.ycor()
    if y > -280:
        player.sety(y - 20)


def move_left():
    """Oyuncuyu sola hareket ettirir"""
    x = player.xcor()
    if x > -380:
        player.setx(x - 20)
    player.setheading(180)


def move_right():
    """Oyuncuyu sağa hareket ettirir"""
    x = player.xcor()
    if x < 380:
        player.setx(x + 20)
    player.setheading(0)


def check_collision():
    """Oyuncu ve hedef kaplumbağa arasındaki mesafeyi kontrol eder"""
    global score
    distance = math.sqrt(
        (player.xcor() - target.xcor()) ** 2 + (player.ycor() - target.ycor()) ** 2
    )
    if distance < 20:
        score += 1
        score_display.clear()
        score_display.write(f"Skor: {score}", align="center", font=("Arial", 16, "normal"))
        move_target()


# Tuş kontrolleri
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# İlk hedef konumu
move_target()

# Ana oyun döngüsü
while game_active:
    player.forward(0)  # Ekranı güncelle
    check_collision()

    # Kalan süreyi güncelle
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, game_time - elapsed_time)
    time_display.clear()
    time_display.write(f"Kalan Süre: {remaining_time}", align="center", font=("Arial", 16, "normal"))

    # Oyun süresi dolduğunda
    if remaining_time == 0:
        game_active = False
        player.hideturtle()
        target.hideturtle()
        score_display.goto(0, 0)
        score_display.write(f"Oyun Bitti!\nToplam Skor: {score}", align="center", font=("Arial", 24, "bold"))

screen.mainloop()