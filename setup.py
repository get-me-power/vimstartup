#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='vim-startup',
    version='1.0',
    license="MIT",
    description='Python Distribution Utilities',
    author='IK',
    author_email='ypa.ypa.ypa.t@gmail.com',
    url='https://github.com/kazukazuinaina/vimstartup',
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'vimstartup = vimstartup:main',
        ],
    },
)
