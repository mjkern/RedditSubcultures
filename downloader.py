
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

# print all the submission titles
print("------ top " + str(limit) + " submissions ------")
for submission in reddit.subreddit(subreddit_name).new(limit=limit):
    print(submission.title)
    submissions.append({
        "id": submission.id,
        "title": submission.title
    }, ignore_index=True)
    for comment in submission.comments:
        print("\t" + comment.body)
        comments.append({
            "id": comment.id,
            "body": comment.body
        }, ignore_index=True)

# write the output files
submissions.to_csv("downloads/" + subreddit_name + "-submissions")
comments.to_csv("downloads/" + subreddit_name + "-comments")
