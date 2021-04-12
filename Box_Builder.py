import arcade
box_num = 30
bw = 30
sw = 600
sh = 600

class Box:
    def __init__(self, x, y, side, dx, dy, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.c = c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

#  bounce off left
        if self.x <= bw + self.side/2:
            self.dx *= -1
            self.c = arcade.color.RED
            #  right
        if self.x >= sw - bw - self.side/2:
            self.dx *= -1
            self.c = arcade.color.YELLOW
        #  top
        if self.y >= sh - bw - self.side/2:
            self.dy *= -1
            self.c = arcade.color.GREEN
        #  bottom
        if self.y <= bw + self.side/2:
            self.dy *= -1
            self.c = arcade.color.BLUE
