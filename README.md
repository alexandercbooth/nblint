# nblint
[![Build Status](https://travis-ci.com/alexandercbooth/nblint.svg?token=UDZsiVdppziAsV1HLtLw&branch=master)](https://travis-ci.com/alexandercbooth/nblint)

Lint Jupyter notebooks like a boss
![](boss.gif)

## Installation
```bash
git clone https://github.com/alexandercbooth/nblint.git
python setup.py install
```
or
```bash
pip install git+https://github.com/alexandercbooth/nblint.git
```

## Usage
### Python
Runs pep8 as the default linter and supports pyflakes
```bash
nblint pythonNotebook.ipynb
```
or pyflakes:
```bash
nblint --linter pyflakes pythonNotebook.ipynb
```
Currently supports the following other languages
## Go
```bash
nblint --linter golint goNotebook.ipynb
```
## R
```bash
nblint --linter lintr RNotebook.ipynb
```
## JavaScript (es6)
```bash
nblint --linter eslint jsNotebook.ipynb
```
