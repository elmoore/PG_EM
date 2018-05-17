import pyautogui as pg
import time

pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft', 'up')
pg.typewrite('youtube.com\n')
time.sleep(3)
pg.typewrite('youtube rewind\n')
pg.moveTo(270, 600, 2)
pg.click(270, 600, 2)

