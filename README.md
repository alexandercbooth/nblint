# nblint
[![Build Status](https://travis-ci.com/alexandercbooth/nblint.svg?token=UDZsiVdppziAsV1HLtLw&branch=master)](https://travis-ci.com/alexandercbooth/nblint)

Lint Jupyter notebooks like a boss
---
![](boss.gif)


A simple CLI tool to lint to Jupyter notebooks.
## Installation
with pip
```bash
$ pip install nblint
```

or bleeding edge
```bash
$ git clone https://github.com/alexandercbooth/nblint.git
$ python setup.py install
```


## Usage
### Python
Runs pycodestyle as the default linter and supports pyflakes
```bash
$ nblint pythonNotebook.ipynb
```
or pyflakes:
```bash
$ nblint --linter pyflakes pythonNotebook.ipynb
```
Currently supports the following other languages
## Go
```bash
$ nblint --linter golint goNotebook.ipynb
```
## JavaScript (es6)
```bash
$ nblint --linter eslint jsNotebook.ipynb
```
