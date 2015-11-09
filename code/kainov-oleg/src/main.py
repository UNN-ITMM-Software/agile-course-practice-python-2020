import argparse

from view import view
from cliview import cli_view


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--cli", action="store_true")
    group.add_argument("--gui", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.cli:
        cli_view.CLIView().mainloop()
    elif args.gui:
        view.View().mainloop()
    else:
        print 'Option is required'
