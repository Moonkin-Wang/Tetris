__author__ = 'Administrator'
import Tkinter

class Brick():
    # initialization of bricks
    L_brick = [[0, 0, 1, 0, 1, 1, 1, 2], [0, 1, 1, 1, 2, 1, 2, 0], [0 ,0 ,0 ,1 ,0 ,2 ,1 ,2], [0, 0, 1, 0, 2, 0, 0, 1]]
    J_brick = [[0, 0, 0, 1, 0, 2, 1, 0], [0, 0, 1, 0, 2, 0, 2, 1], [0, 2, 1, 0, 1, 1, 1, 2], [0, 0, 0, 1, 1, 1, 2, 1]]
    Z_brick = [[0, 0, 1, 0, 1, 1, 2, 1], [1, 0, 1, 1, 0, 1, 0, 2], [0, 0, 1, 0, 1, 1, 2, 1], [1, 0, 1, 1, 0, 1, 0, 2]]
    S_brick = [[0, 1, 1, 0, 1, 1, 2, 0], [0, 0, 0, 1, 1, 1, 1, 2], [0, 1, 1, 0, 1, 1, 2, 0], [0, 0, 0, 1, 1, 1, 1, 2]]
    O_brick = [[0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 1, 1]]
    I_brick = [[0, 0, 1, 0, 2, 0, 3, 0], [0, 0, 0, 1 ,0, 2, 0, 3], [0, 0, 1, 0, 2, 0, 3, 0], [0, 0, 0, 1, 0, 2, 0, 3]]
    T_brick = [[0, 1, 1, 1, 2, 1, 1, 0], [0, 0, 0, 1, 0, 2, 1, 1], [0, 0, 1, 0, 2, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1, 2]]
    brick_type = [L_brick, J_brick, Z_brick, S_brick, O_brick, I_brick, T_brick]

    def __init__(self, canvas, color, type):
        self.canvas = canvas
        self.type = type
        self.shape = 0
        self.brick = list()
        self.stop = False   # whether the brick is at the bottom
        self.color = color
        self.pos = list()
        for i in range(0, 7):
            self.brick.insert(i, list())
        for i in range(0, 4):
            # pre-draw the brick
            self.pos.insert(i, list())
            self.brick[self.type].insert(i, self.canvas.create_rectangle(self.brick_type[self.type][self.shape][i * 2] * 20, self.brick_type[self.type][self.shape][i * 2 + 1] * 20, (self.brick_type[self.type][self.shape][i * 2] + 1) * 20, (self.brick_type[self.type][self.shape][i * 2 + 1] + 1) * 20, fill = self.color, width = 2))
            self.canvas.move(self.brick[self.type][i], 200, 40)
        self.x = 0
        self.y = 0
        self.move_limit_x = self.canvas.winfo_width()
        self.move_limit_y = self.canvas.winfo_height()

    def Move(self):     # movement of bricks
        if not(self.stop):      # when the brick is moving
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)     # event of left button pressing
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)       # event of right button pressing
            self.canvas.bind_all('<KeyPress-Up>', self.shape_change)        # event of up button pressing
            self.Fall()
            for i in range(0, 4):
               self.canvas.move(self.brick[self.type][i], self.x, self.y)
            self.x = 0

    def Fall(self):     # falling movement of bricks
        self.y = 0
        for i in range(0, 4):
            self.pos[i] = self.canvas.coords(self.brick[self.type][i])
            if self.pos[i][3] >= self.move_limit_y:     # whether the brick is at the bottom
                self.y = 0
                self.stop = True
                break

    def turn_left(self, event):     # left movement of bricks
        self.x = -20
        for i in range(0, 4):
            self.pos[i] = self.canvas.coords(self.brick[self.type][i])
            if self.pos[i][0] <= 0:     # whether the brick is on the left border
                self.x = 0
                break

    def turn_right(self, event):        # right movement of bricks
        self.x = 20
        for i in range(0, 4):
            self.pos[i] = self.canvas.coords(self.brick[self.type][i])
            if self.pos[i][2] >= self.move_limit_x:     # whether the brick is on the right border
                self.x = 0
                break

    def shape_change(self, event):      # shape change of bricks
        self.shape = (self.shape + 1) % 4
        self.pos[0] = self.canvas.coords(self.brick[self.type][0])
        for i in range(0, 4):
            self.canvas.delete(self.brick[self.type][i])        # delete the ID of the brick before its shape is changed
            # create a new brick with the new shape
            self.brick[self.type][i] = self.canvas.create_rectangle(self.brick_type[self.type][self.shape][i * 2] * 20, self.brick_type[self.type][self.shape][i * 2 + 1] * 20, (self.brick_type[self.type][self.shape][i * 2] + 1) * 20, (self.brick_type[self.type][self.shape][i * 2 + 1] + 1) * 20, fill = self.color, width = 2)
            self.canvas.move(self.brick[self.type][i], self.pos[0][0], self.pos[0][1])



