
# setup
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
limit = 13
subreddit_name = "ww3theories" # set to None to get name at runtime

# get subreddit name
if subreddit_name:
    print("using subreddit: " + subreddit_name)
else:
    subreddit_name = input("subreddit: ")

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

# give feedback
print("got " + str(len(submissions)) + " submissions and " + str(len(comments)) + " comments")

# write the output files
submissions.to_csv("downloads/" + subreddit_name + "-submissions.csv")
comments.to_csv("downloads/" + subreddit_name + "-comments.csv")
