#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='vim-startup',
    version='1.0',
    license="MIT",
    description='Python Distribution Utilities',
    author='IK',
    author_email='ypa.ypa.ypa.t@gmail.com',
    url='https://github.com/kazukazuinaina/vimstartup',
    packages=find_packages(),
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'vimstartup = vimstartup:main',
        ],
    },
)
