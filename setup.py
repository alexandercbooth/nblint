from setuptools import setup

setup(name='nblint',
      version='0.0.3',
      description='Linting Jupyter notebooks',
      url='http://github.com/alexandercbooth/nblint',
      author='Alexander C. Booth',
      license='MIT',
      packages=['nblint'],
      scripts=['bin/nblint', 'bin/nblint.cmd'],
      install_requires=['pycodestyle', 'flake8', 'nbformat'])
