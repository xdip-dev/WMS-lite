import os
import pathlib


def pathMain():
    return pathlib.Path(__file__).parent.parent.absolute()


def pathGeneratorMainToFile(liste: list):
    """ liste should contain the cascade order of the directory to the file"""
    path_main = pathMain()
    path_sql_directory = pathlib.Path(os.path.join(*liste))
    return os.path.join(path_main, path_sql_directory)
