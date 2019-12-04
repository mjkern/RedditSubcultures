
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
    
# a helper to print periodic updates
count_downloaded = 0
last_update_string = ""
print("downloaded ", end="")
def update_count():
    global count_downloaded # don't really know why python requires this...
    global last_update_string # and this
    count_downloaded += 1
    if count_downloaded % count_to_update == 0:
        print("\b" * len(last_update_string), end="") # backspace old update
        last_update_string = str(count_downloaded)
        print(last_update_string, end="")
        

# get submissions and comments
for submission in reddit.subreddit(subreddit_name).new(limit=limit):
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
        comments = comments.append({
            "comment_id": comment.id,
            "submission_id": comment.link_id,
            "user": comment.author,
            "utc": comment.created_utc,
            "score": comment.score,
            "body": comment.body
        }, ignore_index=True)
    update_count()

# give feedback
print()
print("got " + str(len(submissions)) + " submissions and " + str(len(comments)) + " comments")

# write the output files
date_string = datetime.now().strftime("%y.%m.%d-%H:%M:%S")
submissions.to_csv("downloads/" + subreddit_name + "-submissions-" + date_string + ".csv")
comments.to_csv("downloads/" + subreddit_name + "-comments-" + date_string + ".csv")
