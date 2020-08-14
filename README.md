# vimstartup ![CI](https://github.com/kazukazuinaina/vimstartup/workflows/CI/badge.svg?branch=master) ![reviewdog](https://github.com/kazukazuinaina/vimstartup/workflows/reviewdog/badge.svg?branch=master)

This is a CLI command to easily measure the startup speed of the Vim Inspired by [rhysd/vim-startuptime](https://github.com/rhysd/vim-startuptime)

## Installation

1. clone this repo

```
git clone https://github.com/kazukazuinaina/vimstartup
```

2. install with pip

```
cd vimstartup && pip install -e .
```

## Requirement

- `Python` 3.5 or later (Use subprocess)
- `Vim` 7.4.1444 or later (for --not-a-term startup option)
- `Neovim`

## Usage

Simply run the `vimstartup` command!

If you want to measure Neovim's startup speed, simply do the following command.

```
$ vimstartup --nvim
```

All options can be seen by the following command.

```
$ vimstartup -h
```
