# support python3.5以上

import subprocess


def vim_running(vimpath, outfile):
    cmd = []
    cmd += [vimpath, '--startuptime', outfile, '--not-a-term', '-c', 'qall!']
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        return print('Error')
    else:
        return True
