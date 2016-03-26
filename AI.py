__author__ = 'Alireza Omidi <alireza530@gmail.com>'
__license__ = 'MIT'

import sys
from random import choice

class AI:

    # Just change the do_turn function to write your own bot
    # You can define your own functions inside this class

    # This is a random bot and have little chance to win the game :)
    # So go ahead and write yours

    # Everything you need is in Go module
    # Which is passed every cycle as 'go' to do_turn
    def do_turn(self, go):
        liberties = go.liberties()
        # To print debugs, use print as follows
        print(file=sys.stderr)
        print(liberties, file=sys.stderr)
        if liberties:
            x, y = choice(liberties)
            go.place_move(x, y)
            print('place_move %d %d' % (x, y), file=sys.stderr)
        else:
            available = go.available_moves()
            print(available, file=sys.stderr)
            if available:
                x, y = choice(available)
                go.place_move(x, y)
                print('place_move %d %d' % (x, y), file=sys.stderr)
            else:
                go._pass()
                print('pass', file=sys.stderr)