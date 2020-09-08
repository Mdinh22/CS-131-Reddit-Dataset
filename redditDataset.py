# Imports PRAW. If you do not have PRAW installed, please refer to the FAQ
# (to be included when giving to another student)
# If you use PyCharm, type in terminal:
# pip install praw
# pip install --upgrade praw
import praw

# Authentication to Reddit's servers using a Reddit account.
reddit = praw.Reddit(client_id='zSSSh_xVCB2CQg',
                     client_secret='zDlIP1ENlrX08Xlqu_l4FQgfujc',
                     password='orangecoast22',
                     user_agent='Python Test App', 
                     username='cs131praw')

# Obtain an instance of the subreddit object from the API wrapper.
# In this case, we obtain an instance of the /r/learnpython subreddit.
subreddit = reddit.subreddit('learnpython')
# Obtain four posts of the subreddit's "hot" category.
hot_python = subreddit.hot(limit=4)

# Create a list to store our posts.
posts = []


# Define a custom class to store our attributes called from the API Wrapper.
# Left values are self attributes, right values are calls.
class redditPost:
    def __init__(self):
        self.title = submission.title
        self.score = submission.score
        self.ratio = submission.upvote_ratio
        self.comments = submission.num_comments
        self.date = submission.created_utc

# Filtering certain posts. In this case, we filter out stickied posts,
# since they are always on top.
# If a post passes the filter, create an instance of our class and
# add it to our list
for submission in hot_python:
    if submission.stickied == 0:
        posts.append(redditPost())


# For each post in our list,
# print out its relevant attributes in string format.
for i in posts:
    print(i.title)
    print(i.score)
    print(i.ratio)
    print(i.date)
    print(i.comments)

# For each post in our list, print out its attributes as a tuple.
for i in posts:
    subredditTuple = (i.title, i.score, i.ratio,
                      i.date, i.comments)
    print(subredditTuple)
