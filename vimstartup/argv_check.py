import argparse
import platform


def _get_version():
    __version__ = '1.0.0'
    return ('%s Python %s on %s' %
            (__version__, platform.python_version(), platform.system()))


# entry point
def arg_check():
    parser = argparse.ArgumentParser(prog='vimstartup', description='measure the startup speed of the Vim')
    parser.add_argument('-V', '--version', action='version', version=_get_version())
    parser.add_argument('-N', '--nvim', action='store_true', help="Measuring Neovim's startup time")
    parser.add_argument('--extra', nargs=argparse.REMAINDER, help="Vim options")
    args = parser.parse_args()
    return args
