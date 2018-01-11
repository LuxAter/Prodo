class Card(object):
    def __init__(self, string=dict()):
        self.name = str()
        self.description = str()
        self.task_list = list()
        self.tags = list()
        self.developers = list()
        self.id = None
        if string:
            self.read(string)

    def __repr__(self):
        return self.name

    def read(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'description' in json:
            self.description = json['description']
        if 'tasks' in json:
            self.task_list = json['tasks']
        if 'tags' in json:
            self.tags = json['tags']
        if 'developers' in json:
            self.developers = json['developers']
        if 'id' in json:
            self.id = json['id']

    def write(self):
        json = dict()
        if self.name:
            json['name'] = self.name
        if self.description:
            json['description'] = self.description
        if self.task_list:
            json['tasks'] = self.task_list
        if self.tags:
            json['tags'] = self.tags
        if self.developers:
            json['developers'] = self.developers
        if self.id:
            json['id'] = self.id
        return json

    def display(self, fmt="%i. %n (\033[3m%dv\033[23m)"):
        string = str()
        i = 0
        while i < len(fmt):
            if fmt[i] == '%':
                i += 1
                if fmt[i] == 'n':
                    string += self.name
                    i += 1
                elif fmt[i] == 'i':
                    string += repr(self.id)
                    i += 1
                elif fmt[i] == 'd' and fmt[i+1] == 's':
                    string += self.description
                    i += 2
                elif fmt[i] == 'd' and fmt[i+1] == 'v':
                    string += ' '.join(self.developers)
                    i += 2
                elif fmt[i] == 't' and fmt[i+1] == 'k':
                    string += ' '.join(self.task_list)
                    i += 2
                elif fmt[i] == 't' and fmt[i+1] =='g':
                    string += ' '.join(self.tags)
                    i += 2
                else:
                    string += '%' + fmt[i]
                    i += 1
            else:
                string += fmt[i]
                i += 1
        return string
