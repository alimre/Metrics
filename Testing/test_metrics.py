import unittest
import metrics
import pandas as pd
import numpy as np
import datetime
import tncmme
import tncmmi
import tnf
import tnic
import tnie
import tnl
import tnrc
import tnrr
import tnrvwr
import tna
import clod
import cred
import tnd
import ls
import mrgds
import mrgdd
import mstat
import mclod
import tnmci
import mcred
import mdod
import ms
import prn
import prs
import ud
import tnp
import tnfc

df = pd.read_csv("datax.csv")

class TestMetrics(unittest.TestCase):
    
    def test_number_of_comm3nts(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # comments: 6
        self.assertEqual(tncmme.number_of_comm3nts(df["link"].iloc[260]), 2)
        
    def test_number_of_comm1ts(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # commits: 18
        self.assertEqual(tncmmi.number_of_comm1ts(df["link"].iloc[260]), 18)
        
    def test_number_of_files(self):
        # random index: 260`
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # changed_files: 22
        self.assertEqual(tnf.number_of_files(df["link"].iloc[260]), 22)
        
    def test_number_of_issue_comments(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # issue comments: 6
        self.assertEqual(tnic.number_of_issue_comments(df["link"].iloc[260]), 6)

    def test_number_of_issue_events(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # issue events: 14
        self.assertEqual(tnie.number_of_issue_events(df["link"].iloc[260]), 14)
        
    def test_number_of_labels(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # labels: 2
        self.assertEqual(tnl.number_of_labels(df["link"].iloc[260]), 2)
    
    def test_number_of_review_comm3nts(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # review comments: 2
        self.assertEqual(tnrc.number_of_review_comm3nts(df["link"].iloc[260]), 2)

    def test_number_of_review_requests(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # review comments: 4
        self.assertEqual(tnrr.number_of_review_requests(df["link"].iloc[260]), 4)
    
    def test_number_of_reviewers(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # len(set([review.user.login for review in pull.get_reviews()])): 2
        self.assertEqual(tnrvwr.number_of_reviewers(df["link"].iloc[260]), 2)        
    
    def test_number_of_additions(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["additions"]: 136
        self.assertEqual(tna.number_of_additions(df["link"].iloc[260]), 136)   
    
    def test_closure_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["closed_at"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2022, 1, 10, 17, 36, 15)
        self.assertEqual(clod.closure_date(df["link"].iloc[260]), datetime.datetime(2022, 1, 10, 17, 36, 15))
    
    def test_creation_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["created_at"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2022, 1, 10, 17, 36, 15)
        self.assertEqual(cred.creation_date(df["link"].iloc[260]), datetime.datetime(2022, 1, 9, 17, 21, 56))
    
    def test_number_of_deletions(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["deletions"]: 102
        self.assertEqual(tnd.number_of_deletions(df["link"].iloc[260]), 102)  
    
    def test_locked_state(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["locked"]: False
        self.assertEqual(ls.locked_state(df["link"].iloc[260]), False) 
    
    def test_merged_state(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["merged"]: 102
        self.assertEqual(mrgds.merged_state(df["link"].iloc[260]), True) 
    
    def test_merged_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["merged_at"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2022, 1, 10, 17, 36, 15)
        self.assertEqual(mrgdd.merged_date(df["link"].iloc[260]), datetime.datetime(2022, 1, 10, 17, 36, 15)) 
    
    def test_milestone_status(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["milestone"] != None: True
        self.assertEqual(mstat.milestone_status(df["link"].iloc[260]), True)

    def test_milestone_closure_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["milestone"]["closed_at"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2022, 1, 16, 17, 28, 34)
        self.assertEqual(mclod.milestone_closure_date(df["link"].iloc[260]), datetime.datetime(2022, 1, 16, 17, 28, 34))
    
    def test_number_of_milestone_closed_issues(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["milestone"]["closed_issues"]: 84
        self.assertEqual(tnmci.number_of_milestone_closed_issues(df["link"].iloc[260]), 84)
    
    def test_milestone_creation_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["milestone"]["created_at"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2021, 12, 4, 15, 51, 20)
        self.assertEqual(mcred.milestone_creation_date(df["link"].iloc[260]), datetime.datetime(2021, 12, 4, 15, 51, 20))
    
    def test_milestone_due_on_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["milestone"]["due_on"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2022, 1, 14, 8, 0)
        self.assertEqual(mdod.milestone_due_on_date(df["link"].iloc[260]), datetime.datetime(2022, 1, 14, 8, 0))
    
    def test_milestone_state(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["milestone"]["state"]: closed
        self.assertEqual(ms.milestone_state(df["link"].iloc[260]), "closed")
    
    def test_pull_request_number(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["number"]: 10557
        self.assertEqual(prn.pull_request_number(df["link"].iloc[260]), 10557)
    
    def test_pull_request_state(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # pull.raw_data["state"]: closed
        self.assertEqual(prs.pull_request_state(df["link"].iloc[260]), "closed")
    
    def test_update_date(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # datetime.datetime.strptime(pull.raw_data["updated_at"], "%Y-%m-%dT%H:%M:%SZ"): datetime.datetime(2022, 1, 10, 17, 36, 20)
        self.assertEqual(ud.update_date(df["link"].iloc[260]), datetime.datetime(2022, 1, 10, 17, 36, 20))
    
    def test_number_of_participants(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # participants_in_commits = [commit.author.login for commit in pull.get_commits()] 
        # repo_and_pull_participants = [pull.base.repo.owner.login, pull.base.user.login, pull.head.user.login, pull.user.login]
        # len(list(set(participants_in_commits + repo_and_pull_participants))) : 3
        self.assertEqual(tnp.number_of_participants(df["link"].iloc[260]), 3)
    
    def test_number_of_file_changes(self):
        # random index: 260
        # random pull request: https://github.com/JMRI/JMRI/pull/10557
        # participants_in_commits = [commit.author.login for commit in pull.get_commits()] 
        # if int(pull.get_commits().totalCount)!=0:
        # total_number_of_file_changes = sum([every_file.changes for every_commit in pull.get_commits() for every_file in every_commit.files]): 600
        self.assertEqual(tnfc.number_of_file_changes(df["link"].iloc[260]), 600)
    

if __name__ == '__main__':
    unittest.main()