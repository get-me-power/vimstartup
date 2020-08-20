from vimstartup.measure import start_measure


def entry_point(args):
    if args.nvim:
        start_measure("nvim", args.extra)
    else:
        start_measure("vim", args.extra)
