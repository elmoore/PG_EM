import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=MloJx8bAcOw", "https://www.youtube.com/watch?v=_EvMYEfF_hQ"]

music = ["https://open.spotify.com/album/6kf46HbnYCZzP6rjvQHYzg", "https://open.spotify.com/user/spotify/playlist/37i9dQZF1DXcBWIGoYBM5M"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch videos
b) listen to music

"""
   )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
        
elif answer == "b":
    for i in music:
        webbrowser.open(i)
        
