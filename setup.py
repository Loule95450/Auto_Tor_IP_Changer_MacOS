from setuptools import setup

APP = ["app.py"]
DATA_FILES = ["autoTOR.py"]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app", "thread6"],
)
