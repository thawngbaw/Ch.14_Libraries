
import arcade
import random

from Box_Builder import *




class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.boxlist = []   #  hold all boxes
        for i in range(box_num):
            s = random.randint(10, 50)
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            x = random.randint(bw+s//2, sw-bw-s//2)
            y = random.randint(bw+s//2, sh-bw-s//2)
            c = arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx = 20

            box = Box(x, y, s, dx, dy, c)
            self.boxlist.append(box)


    def on_draw(self):
        arcade.start_render()
        for box in self.boxlist:
            box.draw_box()
        arcade.draw_rectangle_filled(bw//2, sh//2, bw, sh, arcade.color.RED)
        arcade.draw_rectangle_filled(sw-bw//2, sh//2, bw, sh, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(sw//2, sh-bw//2, sw, bw, arcade.color.GREEN)
        arcade.draw_rectangle_filled(sw//2, bw//2, sw, bw, arcade.color.BLUE)


    def on_update(self, dt):
        for box in self.boxlist:
            box.update_box()


def main():
    my_window = MyGame(sw, sh, "30 boxes")

    arcade.run()


if __name__ == "__main__":
    main()