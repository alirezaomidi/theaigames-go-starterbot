# python3

__author__ = 'Alireza Omidi <alireza530@gmail.com>'
__license__ = 'MIT'


from Go import Go
from AI import AI

class Controller:

    def __init__(self):
        self.FUNCTIONS = {
            'settings': self.settings,
            'update': self.update,
            'action': self.action
        }
        self.go = Go()
        self.ai = AI()

    def settings(self, msg):
        _type, value = msg
        if _type == 'player_names':
            value = value.split(',')
        elif _type != 'your_bot':
            value = int(value)
        if _type.startswith('your'):
            _type = _type.replace('your', 'my')
            if _type == 'my_botid':
                self.go.opponent_botid = 3 - value
            elif _type == 'my_bot':
                self.go.opponent_bot = 'player%d' % (3 - int(value[-1]))
        setattr(self.go, _type, value)

    def update(self, msg):
        player, _type, value = msg
        if player == 'game':
            if _type == 'field':
                value = list(map(int, value.split(',')))
                field = []
                for i in range(self.go.field_height):
                    start = i * self.go.field_width
                    end = start + self.go.field_width
                    field.append(value[start:end])
                value = field

            else:
                value = int(value)
        else:
            if player.endswith(str(self.go.my_botid)):
                _type = 'my_points'
            elif player.endswith(str(self.go.opponent_botid)):
                _type = 'opponent_points'
            value = int(value)
        setattr(self.go, _type, value)


    def action(self, msg):
        self.go.timebank = int(msg[-1])
        try:
            self.ai.do_turn(self.go)
        except Exception as e:
            print(e)

    def run(self):
        while True:
            msg = input()
            msg = msg.split()
            try:
                self.FUNCTIONS[msg[0]](msg[1:])
            except Exception as e:
                print(e)

if __name__ == '__main__':
    Controller().run()