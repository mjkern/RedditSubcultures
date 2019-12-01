
# initialization
import praw
reddit = praw.Reddit()

# constants
limit = 13
subreddit_name = None # set to None to get name at runtime

# user input
if subreddit_name:
    print("using subreddit: " + subreddit_name)
else:
    subreddit_name = input("subreddit: ")

# print all the submission titles
print("------ top " + str(limit) + " posts ------")
for submission in reddit.subreddit(subreddit_name).hot(limit=limit):
    print(submission.title)

