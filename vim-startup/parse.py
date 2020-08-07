import subprocess


def vim_time_parse(filepath):
    return subprocess.check_output(['tail', '-1', filepath])
