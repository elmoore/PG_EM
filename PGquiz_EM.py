

import pyautogui as pg

answer = pg.prompt("""
Which way do you want to go?
Left
Right
Middle

""")

# Tells player their choice
pg.alert("You chose " + answer)


if answer == "Left":
    pg.alert("You gain 1 point!")
    points += 1
elif answer == "Right":
    pg.alert("You gain 2 points! Unless your name is ANNIE, then game over!!;)")
    points += 2
elif answer == "Middle":
    pg.alert("You lose 4 points! Suck it annie :)")
    points += -4
    
    
    
