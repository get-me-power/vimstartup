import argparse
import platform
from vimstartup.measure import start_measure


def _get_version():
    __version__ = '1.0.0'
    return ('%s Python %s on %s' %
            (__version__, platform.python_version(), platform.system()))


def arg_check():
    parser = argparse.ArgumentParser(prog='vimstartup', description='measure the startup speed of the Vim')
    parser.add_argument('-V', '--version', action='version', version=_get_version())
    parser.add_argument('-N', '--nvim', action='store_true', help="Measuring Neovim's startup time")
    args = parser.parse_args()
    # Todo : running neovim
    if args.nvim:
        start_measure("nvim")
    else:
        start_measure("vim")
