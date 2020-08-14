import subprocess


def is_neovim(vimpath):
    if 'nvim' in str(vimpath):
        return True
    else:
        return False


def vim_running(vimpath, outfile):
    cmd = []
    if is_neovim(vimpath):
        cmd += [vimpath, '--startuptime', outfile, '--headless', '-c', 'qall!']
    else:
        cmd += [vimpath, '--startuptime', outfile, '--not-a-term', '-c', 'qall!']
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        return print('Error')
    else:
        return True
