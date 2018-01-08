import card
import board
import json

def main():
    bd = board.Board(json.load(open('prodo.json')))
    json.dump(bd.write(), open('prodo.json', 'w'))
    #  print(bd.write())
    bd.display("%i: %n \033[3m(%dv)\033[0m")
    #  print(bd.display("%n (%dv)"))
    #  print(bd.columns[0].cards[0].display("%n (%dv)"))
    #  cd = card.Card()
    #  cd.name = "Prodo"
    #  cd.description = "Kanban/Scrum development tracker"
    #  cd.developers = ["Arden Rasmussen(Nedra1998)"]
    #  cd.task_list = [(False, "Cards"), (False, "Boards"), (False, "Local Files")]
    #  cd.tags = [Tags.FEATURE]
    #  print(cd.write())

if __name__ == "__main__":
    main()
