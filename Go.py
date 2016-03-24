__author__ = 'Alireza Omidi <alireza530@gmail.com>'
__license__ = 'MIT'

class Go:

    def __init__(self):
        self.timebank = 0
        self.time_per_move = 0
        self.player_names = []
        self.my_bot = ''
        self.my_botid = 0
        self.field_width = 0
        self.field_height = 0
        self.round = 0
        self.move = 0
        self.field = []
        self.player1_points = 0
        self.player2_points = 0

    def place_move(self, x, y):
        print('place_move %d %d' % (x, y))

    def _pass(self):
        print('pass')

    def print_all(self):
        print('timebank = %d' % self.timebank)
        print('time_per_move = %d' % self.time_per_move)
        print('player_names = %s' % str(self.player_names))
        print('my_bot = %s' % self.my_bot)
        print('my_botid = %d' % self.my_botid)
        print('field_width = %d' % self.field_width)
        print('field_height = %d' % self.field_height)
        print('round = %d' % self.round)
        print('move = %d' % self.move)
        print('field = %s' % str(self.field))
        print('player1_points = %d' % self.player1_points)
        print('player2_points = %d' % self.player2_points)
        print()