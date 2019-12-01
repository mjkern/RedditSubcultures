
# setup
import praw
reddit = praw.Reddit()

import pandas as pd
submissions = pd.DataFrame(columns=[
    "id",
    "user",
    "date",
    "score",
    "title",
    "body",
    "subreddit"
])

comments = pd.DataFrame(columns=[
    "id",
    "submission_id",
    "user",
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
        "id": submission.id,
        "user": submission.author,
        "date": submission.created_utc,
        "score": submission.score,
        "title": submission.title,
        "body": submission.selftext,
        "subreddit": submission.subreddit.display_name
    }, ignore_index=True)
    for comment in submission.comments:
        comments = comments.append({
            "id": comment.id,
            "submission_id": comment.parent_id, # for nested comments this would be a comment id, but currently not getting nested comments
            "user": comment.author,
            "score": comment.score,
            "body": comment.body
        }, ignore_index=True)

# give feedback
print("got " + str(len(submissions)) + " submissions and " + str(len(comments)) + " comments")

# write the output files
submissions.to_csv("downloads/" + subreddit_name + "-submissions.csv")
comments.to_csv("downloads/" + subreddit_name + "-comments.csv")
