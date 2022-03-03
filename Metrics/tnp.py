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
    
def number_of_participants(link):
    """
    ----------------------------------
    Total Number of Participants (TNP)
    ----------------------------------
    The total amount of users participating within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            participants_in_commits = [commit.author.login for commit in pull.get_commits()]
            repo_and_pull_participants = [pull.base.repo.owner.login, pull.base.user.login, pull.head.user.login, pull.user.login]
            return len(list(set(participants_in_commits + repo_and_pull_participants)))
            
        except:
            return 0
            
    return action()