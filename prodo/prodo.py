from prodo.project import Project
import prodo.actions as actions
import json
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Project development software")
    parser.add_argument('--version', action='version', version='%(prog)s 0.0')
    parser.add_argument('--list', action='store_true',
                        help="Lists all past and active sprints")
    parser.add_argument('--sprint', nargs='?', type=int, default=1,
                        help="Select sprint to focus on (default \'Current\')")
    subparsers = parser.add_subparsers(
        help="Different actions commands", dest='command')
    add = subparsers.add_parser('add')
    add.add_argument('name', nargs='?', help="Task name to add")
    add.add_argument('description', nargs='?', help="Task description")
    add.add_argument('--tasks', nargs='*', help="Sub tasks to complete")
    add.add_argument('--tags', nargs='*', help="Tags to categorize task")
    add.add_argument('--dev', nargs='*', help="Name of assigned developer")
    mod = subparsers.add_parser('modify')
    mod.add_argument('id', type=int, help="Id identifier of task in sprint")
    mod.add_argument('name', nargs='?', help="Task name")
    mod.add_argument('description', nargs='?', help="Task description")
    mod.add_argument('--tasks', nargs='*', help="Sub tasks to complete")
    mod.add_argument('--tags', nargs='*', help="Tags to categorize task")
    mod.add_argument('--dev', nargs='*', help="Name of assigned developer")
    dlt = subparsers.add_parser('delete')
    dlt.add_argument('id', type=int, help="Id of task in sprint to delete")
    move = subparsers.add_parser('move')
    move.add_argument('id', type=int, help="Id identifier of task in sprint")
    move.add_argument('column', nargs='?',
                      help="Destination column to place task")
    new = subparsers.add_parser('new')
    new.add_argument('object', type=str, choices=[
                     "column", "sprint"], help="Object to create new of")
    new.add_argument('name', nargs='?', help="Name of new object")
    lst = subparsers.add_parser('list')
    start = subparsers.add_parser('start')
    args = parser.parse_args()
    print(args)
    proj = Project(json.load(open('prodo.json')))
    actions.preform_action(proj, args)
    json.dump(proj.write(), open('prodo.json', 'w'))


if __name__ == "__main__":
    main()
