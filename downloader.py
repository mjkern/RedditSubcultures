
# setup
from datetime import datetime
import praw
reddit = praw.Reddit()

import pandas as pd
submissions = pd.DataFrame(columns=[
    "submission_id",
    "user",
    "utc",
    "score",
    "title",
    "body",
    "subreddit"
])

comments = pd.DataFrame(columns=[
    "comment_id",
    "submission_id",
    "user",
    "utc",
    "score",
    "body"
])

# constants
limit = 100000 # I suspect reddit will cap me out at some point
subreddit_name = None # set to None to get name at runtime
count_to_update = 10

# get subreddit name
if subreddit_name:
    print("using subreddit: " + subreddit_name)
else:
    subreddit_name = input("subreddit: ")
    
# get submissions and comments
number_downloaded = 0
for submission in reddit.subreddit(subreddit_name).new(limit=limit):
    try:
        submissions = submissions.append({
            "submission_id": submission.id,
            "user": submission.author,
            "utc": submission.created_utc,
            "score": submission.score,
            "title": submission.title,
            "body": submission.selftext,
            "subreddit": submission.subreddit.display_name
        }, ignore_index=True)
        for comment in submission.comments:
            try:
                comments = comments.append({
                    "comment_id": comment.id,
                    "submission_id": comment.link_id,
                    "user": comment.author,
                    "utc": comment.created_utc,
                    "score": comment.score,
                    "body": comment.body
                }, ignore_index=True)
            except:
                print("one failed comment")
        # update count
        number_downloaded += 1
        print("downloaded " + str(number_downloaded), end="\r") # \r causes the next print to overwrite this one
    except:
        print("one failed submission")

# give feedback
print()
print("got " + str(len(submissions)) + " submissions and " + str(len(comments)) + " comments")

# write the output files
date_string = datetime.now().strftime("%y.%m.%d-%H:%M:%S")
submissions.to_csv("downloads/" + subreddit_name + "-submissions-" + date_string + ".csv")
comments.to_csv("downloads/" + subreddit_name + "-comments-" + date_string + ".csv")
