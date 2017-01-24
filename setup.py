from setuptools import setup

setup(name='nblint',
      version='0.0.1',
      description='Linting Jupyter notebooks',
      url='http://github.com/alexandercbooth/nblint',
      author='Alexander C. Booth',
      author_email='alexander.c.booth@gmail.com',
      license='MIT',
      packages=['nblint'],
      scripts=['bin/nblint', 'bin/nblint.cmd', 'nbformat'],
      install_requires=['pep8', 'flake8'])
