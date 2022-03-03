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

def number_of_milestone_closed_issues(link):
    """
    -----------------------------------------------
    Total Number of Milestone Closed Issues (TNMCI)
    -----------------------------------------------
    The total amount of closed issued related to the milestone within the pull request.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.raw_data["milestone"]["closed_issues"]

        except:
            return None

    return action()