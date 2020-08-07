import tempfile
import os
import run_vim

with tempfile.TemporaryDirectory() as dname:
    print(dname)                 # /tmp/tmpl2cvqpq5
    print(os.path.exists(dname))
    run_vim.vim_running('/usr/local/bin/vim', dname + 'vim_start.log')
    print(os.path.exists(dname))
print(os.path.exists(dname))     # False
