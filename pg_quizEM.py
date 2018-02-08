import pyautogui as pg
import time
import webbrowser

points = 0


# Question

answer = pg.prompt(
"""
What describes you best?

a) resilient
b) you know what you want
c) caring
d) mean until you get to know me

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


# Question 2

answer = pg.prompt(
"""
What do you do when something bad happens?

a) I dance or run away
b) I stop talking and don't leave my house
c) BAKE
d) become agressive

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


# Question 3

answer = pg.prompt(
"""
What color hair do you have?

a) red
b) black
c) blond
d) brown

"""
    )


# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4



# Question 4

answer = pg.prompt(
"""
Who would you most likely marry?

a) Someone you met at a bar
b) Your boss
c) Someone you're helping
d) Your enemy turned friend

"""
    )


# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


# Question 5

answer = pg.prompt(
"""
How many kids do you want?

a) 3
b) I hate kids!
c) I have one
d) Not sure yet

""")

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4
#END OF SURVEY

pg.alert("you are...")
#meredith
if points < 10:
    pg.alert("Meredith Grey")
    webbrowser.open("https://media.giphy.com/media/qlN5E8jnuGOs/giphy.gif")


#christina
elif points >= 10 and points < 12:
    pg.alert("Christina Yang")
    webbrowser.open("https://78.media.tumblr.com/aafa2643006ef1c8e27b91471755d01f/tumblr_oiepy424MU1vz0o29o1_500.gif")
    


#izzie
elif points >= 12 and points < 16:
    pg.alert("Izzie Stevens")
    webbrowser.open("https://em.wattpad.com/03e79e62a07e3344af9676ba56e8c5c6edf59fbe/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f716b45756a5167664e67694656513d3d2d3332303133323939382e313437626231343364383230383037333434393439303638373936342e676966?s=fit&w=720&h=720")
    

#alex
elif points >= 16 and points < 21:
    pg.alert("Izzie Stevens")
    webbrowser.open("https://img.buzzfeed.com/buzzfeed-static/static/2016-09/8/20/asset/buzzfeed-prod-web08/anigif_sub-buzz-1734-1473381808-2.gif")



