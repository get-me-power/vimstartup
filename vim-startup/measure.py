import tempfile
import os
import run_vim
import parse


def main():
    with tempfile.TemporaryDirectory() as dname:
        run_vim.vim_running('/usr/local/bin/vim', dname + 'vim_start.log')
        if os.path.exists(dname + 'vim_start.log'):
            print(parse.vim_time_parse(dname + 'vim_start.log'))
        else:
            print('Error')
