import subprocess

out = subprocess.Popen(["nblint", "../examplenbs/py.ipynb"],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT
                       ).communicate()[0]

out2 = subprocess.Popen(["nblint", "../examplenbs/py.ipynb",
                        "--linter", "pyflakes"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT
                        ).communicate()[0]

with open("pycodestyle.txt", "r") as f:
    ff = f.read()

with open("pyflakes.txt", "r") as f2:
    ff2 = f2.read()


def test_pycodestyle():
    assert ff == out.decode("utf8")


def test_pyflakes():
    assert ff2 == out2.decode("utf8")
