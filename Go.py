__author__ = 'Alireza Omidi <alireza530@gmail.com>'
__license__ = 'MIT'

class Go:

    def __init__(self):
        self.timebank = 0
        self.time_per_move = 0
        self.player_names = []
        self.my_bot = ''
        self.my_botid = 0
        self.opponent_bot = ''
        self.opponent_botid = 0
        self.field_width = 0
        self.field_height = 0
        self.round = 0
        self.move = 0
        self.field = []
        self.my_points = 0
        self.opponent_points = 0

    def place_move(self, x, y):
        if self.field[x][y] == 1:
            pass  # TODO not valid
        print('place_move %d %d' % (x, y))

    def _pass(self):
        print('pass')

    def is_empty(self, x, y):
        return self.field[x][y] == 0

    def liberties(self, srcx=None, srcy=None):
        if srcx is None and srcy is None:
            libs = set()
            for i in range(self.field_width):
                for j in range(self.field_height):
                    if self.field[i][j] == self.my_botid:
                        libs.update(self.liberties(i, j))
            return list(libs)

        stack = [(srcx, srcy)]
        visited = {(srcx, srcy)}
        libs = []
        while stack:
            x, y = stack.pop()
            if self.field[x][y] != self.my_botid:
                if self.field[x][y] == 0:
                    libs.append((x, y))
            else:
                relative_neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for relx, rely in relative_neighbours:
                    neix, neiy = x + relx, y + rely
                    if (neix, neiy) not in visited and \
                            0 <= neix < self.field_width and 0 <= neiy < self.field_height:
                        stack.append((neix, neiy))
                        visited.add((neix, neiy))
        return libs

    def is_suicide(self, x, y):
        if not self.is_empty(x, y):
            pass  # TODO not valid
        self.field[x][y] = self.my_botid
        libs = self.liberties(x, y)
        self.field[x][y] = 0
        return len(libs) == 0

    def available_moves(self):
        moves = []
        for i in range(self.field_width):
            for j in range(self.field_height):
                if self.is_empty(i, j) and not self.is_suicide(i, j):
                    moves.append((i, j))
        return moves

    def print_all(self):
        print('timebank = %d' % self.timebank)
        print('time_per_move = %d' % self.time_per_move)
        print('player_names = %s' % str(self.player_names))
        print('my_bot = %s' % self.my_bot)
        print('my_botid = %d' % self.my_botid)
        print('opponent_bot = %s' % self.opponent_bot)
        print('opponent_botid = %d' % self.opponent_botid)
        print('field_width = %d' % self.field_width)
        print('field_height = %d' % self.field_height)
        print('round = %d' % self.round)
        print('move = %d' % self.move)
        print('field = %s' % str(self.field))
        print('my_points = %d' % self.my_points)
        print('opponent_points = %d' % self.opponent_points)
        print()