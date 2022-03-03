import os
import subprocess
import sys
import numpy as np 
import datetime 
from subprocess import STDOUT, check_call 
import os 
from getOutScript import getOut

# subprocess.check_call(['apt', 'install', '-qq', 'enchant'], stdout=open(os.devnull,'wb'), stderr=STDOUT) 
# subprocess.check_call([sys.executable, "-m", "pip", "install", "pyenchant"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "PyGithub"])

from github import Github
g = Github("")

# import enchant
# d = enchant.Dict("en_US")

def getOut(repo_link):
    other, pull = os.path.split(repo_link)
    other, _ = os.path.split(other)
    repo_name = other[19:]
    return repo_name, int(pull)
    
def update_date(link):
    """
    ----------------
    Update Date (UD)
    ----------------
    The date on which the pull request was updated.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            # return pull.raw_data["updated_at"]
            return datetime.datetime.strptime(pull.raw_data["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
        
        except:
            return None
    
    return action()