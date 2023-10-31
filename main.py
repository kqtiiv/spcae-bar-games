import time
import turtle

FONT = ("Arial", 10, "normal")
GAME2_TIME_LIMIT = 5
SPACE_PRESS_GOAL = 100

screen = turtle.Screen()
screen.title("Spacebar games!")


turtle.hideturtle()
turtle.up()
turtle.goto(-175,0)

start = 0
space_press = 0
turtle.write("Press Left for Space Game 1 Right for Space Game 2", font=FONT)

game1_playing = False
game1_end = False

game2_playing = False
game2_end = False
timer_active = False


def left():
  global game1_playing, start
  game1_playing = True
  start = time.time()
  turtle.clear()
  turtle.goto(-100,0)
  turtle.write("Click space as much as possible", font=FONT)
  

def right():
  global game2_playing, start
  game2_playing = True
  start = time.time()
  turtle.clear()
  turtle.goto(-100,0)
  turtle.write("Click space as much as possible", font=FONT)


def activate_timer():
  global game2_end, timer_active
  timer_active = True
  time_limit = GAME2_TIME_LIMIT
  for i in range(time_limit):
    turtle.clear()
    turtle.goto(-100, 0)
    turtle.write(f"Seconds remaining: {time_limit-i}", font=FONT)
    time.sleep(1)
  game2_end = True


def space():
  global space_press, timer_active, game1_playing, game2_playing
  space_press_goal = SPACE_PRESS_GOAL
  if game1_playing:
    space_press += 1
    turtle.clear()
    turtle.goto(-75, 0)
    turtle.write(f"Space presses: {space_press}", font=FONT)
  elif game2_playing:
    space_press += 1
    if timer_active is False:
      activate_timer()
    if game2_end:
      turtle.clear()
      turtle.goto(-15,0)
      turtle.write(str(space_press) + " Presses!", font=FONT)
      game2_playing = False
    
    
  if space_press >= space_press_goal:
    end = time.time()
    turtle.clear()
    turtle.goto(-50,0)
    turtle.write("Time is " + str(round(end-start,2)) + " seconds!", font=FONT)
    game1_playing = False
    space_press = 0


turtle.onkey(space, "space")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")

turtle.listen()
turtle.mainloop()
