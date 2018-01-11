from prodo.card import Card

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

    def find_task(self, id):
        tsk = [x for x in self.cards if x.id == id]
        if len(tsk) == 0:
            return None
        return tsk[0]

    def add(self, args, id):
        card = Card()
        card.name = args.name
        card.description = args.description
        card.task_list = args.tasks
        card.tags = args.tags
        card.developers = args.dev
        card.id = id
        self.cards.append(card)

    def delete(self, id):
        dlt = [x for x in self.cards if x.id == id]
        self.cards = [x for x in self.cards if x not in dlt]
