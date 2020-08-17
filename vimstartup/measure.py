import tempfile
import os
import sys
from vimstartup.parse import vim_time_parse
from vimstartup.run_vim import vim_running
from vimstartup.path_check import checkpath


def start_measure(command, vim_option):
    with tempfile.TemporaryDirectory() as dname:
        vim_running(checkpath(command), dname + 'vim_start.log', vim_option)
        if os.path.exists(dname + 'vim_start.log'):
            print(vim_time_parse(dname + 'vim_start.log'))
        else:
            sys.exit('Failed to create a file to record the results.')
