from card import Card

class Column(object):
    def __init__(self, string=dict()):
        self.name = str()
        self.cards = list()
        if string:
            self.read(string)

    def __repr__(self):
        return self.name

    def read(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'cards' in json:
            for card in json['cards']:
                self.cards.append(Card(card))

    def write(self):
        json = dict()
        if self.name:
            json['name'] = self.name
        if self.cards:
            json['cards'] = list()
            for card in self.cards:
                json['cards'].append(card.write())
        return json
