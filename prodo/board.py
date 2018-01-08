import os
from ioterm.table import Table
from ioterm import display
from column import Column
from tag import Tag

class Board(object):
    def __init__(self, string=dict()):
        self.name = str()
        self.columns = list()
        self.tags = list()
        if string:
            self.read(string)

    def __repr__(self):
        return self.name

    def read(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'columns' in json:
            for col in json['columns']:
                self.columns.append(Column(col))
        if 'tags' in json:
            for tg in json['tags']:
                self.tags.append(Tag(tg))

    def write(self):
        json = dict()
        if self.name:
            json['name'] = self.name
        if self.columns:
            json['columns'] =list()
            for col in self.columns:
                json['columns'].append(col.write())
        if self.tags:
            json['tags'] = list()
            for tg in self.tags:
                json['tags'].append(tg.write())
        return json

    def display(self, fmt):
        data = list()
        for i, col in enumerate(self.columns):
            data.append([col.name])
            for j, el in enumerate(col.cards):
                data[i].append(el.display(fmt))
        tb = Table()
        tb.data = data
        tb.col_pri = True
        tb.flags["zebra"] = True
        tb.fmt = tb.BoxFormat.UNICODE
        tb.flags["vert_sep"] = True
        tb.row_align(0, 'c')
        tb.flags["title_row"] = [0]
        tb.flags["same_width"] = True
        #  tb.flags["min_height"] = 20
        tb.flags["set_width"] = 'Full'
        tb.title_fmt =["\033[1;4m", "\033[21;24m"]
        width = int(os.popen("stty size", "r").read().split()[1])
        print(display.print_aligned("\033[1m" + self.name + "\033[0m", 'c', width))
        tb.display()
