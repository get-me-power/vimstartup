import subprocess
import sys


def is_neovim(vimpath):
    if 'nvim' in str(vimpath):
        return True
    else:
        return False


def vim_running(vimpath, outfile, vim_option):
    cmd = []
    if is_neovim(vimpath):
        cmd += [vimpath, '--startuptime', outfile, '--headless']
    else:
        cmd += [vimpath, '--startuptime', outfile, '--not-a-term']
    if vim_option:
        cmd += vim_option
    cmd += ['-c', 'qall!']
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        sys.exit("\nCommand execution failed.")
    else:
        return True
