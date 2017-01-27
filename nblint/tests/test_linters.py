import subprocess
import os


nbPath = os.path.join("nblint", "examplenbs")
testPath = os.path.join("nblint", "tests")

if os.name == 'posix':
    shell = False
else:
    shell = True


out = subprocess.Popen(["nblint", os.path.join(nbPath, "py.ipynb")],
                       stdout=subprocess.PIPE,
                       shell=shell
                       ).communicate()[0].decode('utf8').splitlines()

out2 = subprocess.Popen(["nblint", os.path.join(nbPath, "py.ipynb"),
                        "--linter", "pyflakes"],
                        stdout=subprocess.PIPE,
                        shell=shell
                        ).communicate()[0].decode('utf8').splitlines()


with open(os.path.join(testPath, "pycodestyle.txt"), "r") as f:
    ff = f.read().splitlines()
    ff = list(filter(None, ff))

with open(os.path.join(testPath, "pyflakes.txt"), "r") as f2:
    ff2 = f2.read().splitlines()
    ff2 = list(filter(None, ff2))


def test_pycodestyle():
    assert ff == list(filter(None, out))


def test_pyflakes():
    assert ff2 == list(filter(None, out2))
