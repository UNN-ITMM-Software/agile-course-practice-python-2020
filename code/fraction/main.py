import argparse

from fraction.guiview import gui_view
from fraction.cliview import cli_view


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
        gui_view.GUIView().mainloop()
    else:
        print('Option is required')
