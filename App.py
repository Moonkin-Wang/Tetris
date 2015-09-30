__author__ = 'Administrator'
import Tkinter
import random
import time
from Brick import Brick

tk = Tkinter.Tk()
tk.title("Tetris")
tk.resizable(0, 0)
tk.wm_attributes("-topmost")
canvas = Tkinter.Canvas(tk, width = 400, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()
type = random.randint(0, 7)
#color = ['red', ]
brick = Brick(canvas, 'Cornflower Blue', 6)
while 1:
    brick.Move()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)
tk.mainloop()