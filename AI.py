__author__ = 'Alireza Omidi <alireza530@gmail.com>'
__license__ = 'MIT'

from random import randrange

class AI:

    def do_turn(self, go):
        x = randrange(0, go.field_width)
        y = randrange(0, go.field_height)
        if go.field[x][y] == 0:
            go.place_move(x, y)
        else:
            go._pass()