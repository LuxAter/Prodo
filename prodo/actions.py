def preform_action(project, args):
    print(args.command)
    if args.list is True:
        project.print_sprints()
    elif args.command == 'add':
        project.sprint_add(args.sprint, args)
    elif args.command == 'modify':
        pass
    elif args.command == 'delete':
        project.sprint_delete(args.sprint, args)
    elif args.command == 'move':
        project.sprint_move(args.sprint, args)
    elif args.command == 'new':
        pass
    elif args.command == 'list':
        project.sprint_list(args.sprint)
    elif args.command == 'start':
        pass
    else:
        project.sprint_summary(args.sprint)

