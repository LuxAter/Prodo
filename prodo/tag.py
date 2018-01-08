class Tag(object):
    def __init__(self, string=dict()):
        self.name = str()
        self.color = str()
        if string:
            self.read(string)

    def __repr__(self):
        return self.name

    def read(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'color' in json:
            self.color = json['color']

    def write(self):
        json = dict()
        if self.name:
            json['name'] = self.name
        if self.color:
            json['color'] = self.color
        return json
