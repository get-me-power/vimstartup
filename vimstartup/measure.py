import tempfile
import os
from vimstartup.parse import vim_time_parse
from vimstartup.run_vim import vim_running


def start_measure():
    with tempfile.TemporaryDirectory() as dname:
        vim_running('/usr/local/bin/vim', dname + 'vim_start.log')
        if os.path.exists(dname + 'vim_start.log'):
            print(vim_time_parse(dname + 'vim_start.log'))
        else:
            print('Error')
