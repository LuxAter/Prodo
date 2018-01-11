import ioterm.display as display
from ioterm.table import Table
import ioterm.bar as bar

import datetime
from prodo.board import Board


class Sprint(object):
    def __init__(self, string=dict()):
        self.name = str()
        self.start = datetime.datetime(2018, 1, 1)
        self.end = self.start + datetime.timedelta(days=14)
        self.kanban = Board()
        self.progress = [0, 0]
        self.tasks = dict()
        if string:
            self.read(string)

    def __repr__(self):
        return self.name

    def update_tasks(self):
        for col in self.kanban.columns:
            self.tasks[col] = list()
            for task in col.cards:
                self.tasks[col].append(task)
                self.progress[0] += 1
                if col == self.kanban.columns[-1]:
                    self.progress[1] += 1


    def read(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'start' in json:
            self.start = datetime.datetime.fromtimestamp(json['start'])
        if 'end' in json:
            self.end = datetime.datetime.fromtimestamp(json['end'])
        if 'kanban' in json:
            self.kanban = Board(json['kanban'])
        self.update_tasks()

    def write(self):
        json = dict()
        if self.name:
            json['name'] = self.name
        if self.start:
            json['start'] = self.start.timestamp()
        if self.end:
            json['end'] = self.end.timestamp()
        if self.kanban:
            json['kanban'] = self.kanban.write()
        return json

    def progress_bar(self):
        perc = 0.0
        if self.progress[0] != 0:
            perc = self.progress[1] / self.progress[0]
        print(bar.print_bar(perc))

    def predicted_progress_bar(self):
        perc = (1.0 / 14.0) * 100
        diff = datetime.datetime.now() - self.start
        perc *= diff.days
        print(bar.print_bar(perc))

    def progress_diff(self):
        perc = 0.0
        if self.progress[0] != 0:
            perc = self.progress[1] / self.progress[0] * 100.0
        diff = datetime.datetime.now() - self.start
        exp = (1.0 / (self.end-self.start).days) * diff.days * 100.0
        print(bar.print_bar([perc, exp], colors=['green', 'red', 'black']))

    def list(self, width=79):
        for key, value in self.tasks.items():
            print("\033[1m" + display.print_aligned(key.name,
                                                    'c', width) + "\033[0m")
            lst = [x.display() for x in value]
            display.colprint(lst, 79, True, True, True)

    def summary(self, width=79):
        print("\033[1;4m" + display.print_aligned(self.name,
                                                  'c', width) + "\033[0m")
        self.progress_diff()
        self.list()
        table = Table()
        table.flags['zebra'] = True
        table.flags['title_col'] = [0]
        table.flags['set_width'] = width
        table.data = [["Start Date:", self.start.strftime("%d-%m-%Y")],
                      ["End Date:", self.end.strftime("%d-%m-%Y")]]
        table.display()

    def add(self, args):
        self.kanban.add(args, self.progress[0] + 1)

    def delete(self, args):
        self.kanban.delete(args.id)

    def move(self, args):
        self.kanban.move(args.id, args.column)

