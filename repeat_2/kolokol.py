class Bell():
    def __init__(self, *args, **kwargs):
        self.r = args
        self.s = args
        self.i = 0
        self.ves = args
        self.ves1 = kwargs

    def print_info(self):
        list_keys = list(self.ves1.keys())
        list_keys.sort()
        self.keys_sort = {i: self.ves1[i] for i in list_keys}
        text_print1 = ', '.join(str(key) + ': ' + str(value)
                                for key, value in self.keys_sort.items())
        text_print = ', '.join(
            str(value) for value in self.ves)

        if len(text_print1) > 0 and len(text_print) > 0:
            text_print1 = text_print1 + '; ' + text_print
        elif len(text_print1) > 0 and len(text_print) == 0:
            text_print1 = text_print1
        elif len(text_print) == 0:
            text_print1 = '-'
        else:
            text_print1 = text_print
        print(text_print1)


class BellTower(Bell):

    def append(self, *f):
        self.s = self.s + f

    def sound(self):
        for i in self.s:
            i.sound()
        print('...')


class LittleBell(BellTower):
    def sound(self):
        print('ding')


class BigBell(BellTower):
    def sound(self):
        if self.i == 0:
            print('ding')
            self.i += 1
        else:
            print('dong')
            self.i = 0

