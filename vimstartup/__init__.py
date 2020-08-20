from vimstartup.argv_check import arg_check
from vimstartup.entrypoint import entry_point


def main():
    entry_point(arg_check())


if __name__ == '__main__':
    main()
