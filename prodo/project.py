import ioterm.display as display
from ioterm.menu import Menu
from prodo.sprint import Sprint

class Project(object):
    def __init__(self, string=dict()):
        self.name = str()
        self.sprints = list()
        if string:
            self.read(string)

    def __repr__(self):
        return self.name

    def read(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'sprints' in json:
            self.sprints = list()
            for sprint in json['sprints']:
                self.sprints.append(Sprint(sprint))

    def write(self):
        json = dict()
        if self.name:
            json['name'] = self.name
        if self.sprints:
            json['sprints'] = list()
            for sprint in self.sprints:
                json['sprints'].append(sprint.write())
        return json

    def print_sprints(self):
        sprint_list = [x.name for x in self.sprints]
        menu = Menu()
        menu.name = self.name + " Sprints"
        menu.options = sprint_list
        menu.flags["zebra"] = True
        menu.flags["size"] = 79
        menu.display()

    def sprint_summary(self, sprint):
        self.sprints[sprint - 1].summary()

    def sprint_list(self, sprint):
        self.sprints[sprint - 1].list()

    def sprint_add(self, sprint, args):
        self.sprints[sprint - 1].add(args)

    def sprint_delete(self, sprint, args):
        self.sprints[sprint - 1].delete(args)

    def sprint_move(self, sprint, args):
        self.sprints[sprint - 1].move(args)


