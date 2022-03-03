import os

def getOut(repo_link):
    other, pull = os.path.split(repo_link)
    other, _ = os.path.split(other)
    repo_name = other[19:]
    return repo_name, int(pull)