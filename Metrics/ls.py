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

# def getOut(repo_link):
#     other, pull = os.path.split(repo_link)
#     other, _ = os.path.split(other)
#     repo_name = other[19:]
#     return repo_name, int(pull)
    
def number_of_comm3nts(link):
    """
    ---------------------------------
    Total Number of Comments (TNCMME)
    ---------------------------------
    The total amount of comments within the pull request.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_comments().totalCount
        except:
            return None

    return action()

def number_of_comm1ts(link):
    """
    -------------------------------
    Total Number of Commits (NCMMI)
    -------------------------------
    The total number of commits within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_commits().totalCount
        except:
            return None

    return action()

def number_of_files(link):
    """
    ---------------------------
    Total Number of Files (TNF)
    ---------------------------
    The total amount of files within the pull request.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_files().totalCount
        except:
            return None

    return action()

def number_of_issue_comments(link):
    """
    -------------------------------------
    Total Number of Issue Comments (TNIC)
    -------------------------------------
    The total amount of comments related to issues within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_issue_comments().totalCount
        except:
            return None

    return action()

def number_of_issue_events(link):
    """
    -----------------------------------
    Total Number of Issue Events (TNIE)
    -----------------------------------
    The total amount of issue events related to issues within the pull request.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_issue_events().totalCount
        except:
            return None

    return action()

def number_of_labels(link):
    """
    ----------------------------
    Total Number of Labels (TNL)
    ----------------------------
    The total amount of labels within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_labels().totalCount
        except:
            return None

    return action()

def number_of_review_comm3nts(link):
    """
    --------------------------------------
    Total Number of Review Comments (TNRC)
    --------------------------------------
    The total amount of comments related to the reviews within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.get_review_comments().totalCount
        except:
            return None

    return action()

def number_of_review_requests(link):
    """
    --------------------------------------
    Total Number of Review Requests (TNRR)
    --------------------------------------
    The total amount of requests for a review. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return sum([request.totalCount for request in pull.get_review_requests()])
        except:
            return None

    return action()

def number_of_reviewers(link):
    """
    ----------------------------------
    Total Number of Reviewers (TNRVWR)
    ----------------------------------
    The total amount of users who act as reviewers within the pull request.
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return len(set([review.user.login for review in pull.get_reviews()]))

        except:
            return None
                
    return action()

def number_of_additions(link):
    """
    -------------------------------
    Total Number of Additions (TNA)
    -------------------------------
    The total amount of added lines within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.raw_data["additions"]
        except:
            return None

    return action()

def closure_date(link):
    """
    -------------------
    Closure Date (CLOD)
    -------------------
    The date on which the pull request was closed. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return datetime.datetime.strptime(pull.raw_data["closed_at"], "%Y-%m-%dT%H:%M:%SZ")
            # return pull.raw_data["closed_at"]
            
        except:
            return None

    return action()

def creation_date(link):
    """
    --------------------
    Creation Date (CRED)
    --------------------
    The date on which the pull request was created. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            # return pull.raw_data["created_at"]
            return datetime.datetime.strptime(pull.raw_data["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            
        except:
            return None

    return action()

def number_of_deletions(link):
    """
    -------------------------------
    Total Number of Deletions (TND)
    -------------------------------
    The total amount of deleted lines within the pull request. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.raw_data["deletions"]
            
        except:
            return None

    return action()

def locked_state(link):
    """
    -----------------
    Locked State (LS)
    -----------------
    The locked or unlocked state of the pull request given by its collaborators. 
    """
    repository, pull_request = getOut(link)
    
    def action():
        try:
            repo = g.get_repo(repository)
            pull = repo.get_pull(pull_request)
            return pull.raw_data["locked"]
            
        except:
            return None

    return action()
