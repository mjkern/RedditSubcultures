
import praw
reddit = praw.Reddit()

for submission in reddit.front.hot(limit=10):
    print(submission.score)

