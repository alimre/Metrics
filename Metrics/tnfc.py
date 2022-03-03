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

def number_of_file_changes(link):
    """
    -----------------------------------
    Total Number of File Changes (TNFC) 
    -----------------------------------
    The total amount of file changes within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            if int(pull.get_commits().totalCount)!=0:
                total_number_of_file_changes = sum([every_file.changes for every_commit in pull.get_commits() for every_file in every_commit.files])
                return total_number_of_file_changes
            if int(pull.get_commits().totalCount)==0:
                return 0
        except:
            return None
    
    return action()
