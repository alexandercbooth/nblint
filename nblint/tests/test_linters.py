import subprocess

out = subprocess.Popen(["nblint", "../examplenbs/kmeans.ipynb"],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT
                       ).communicate()[0]

out2 = subprocess.Popen(["nblint", "../examplenbs/kmeans.ipynb",
                        "--linter", "pyflakes"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT
                        ).communicate()[0]

with open("pep8.py", "r") as f:
    ff = f.read()

with open("pyflakes.py", "r") as f2:
    ff2 = f2.read()


def test_pep8():
    assert ff == out.decode("utf8")


def test_pyflakes():
    assert ff2 == out2.decode("utf8")
