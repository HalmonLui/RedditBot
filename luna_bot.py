# author: Halmon Lui
#Counts which subreddit used the name Luna in it

import praw
import time

# Initialize PRAW with a custom user-agent

r = praw.Reddit("/u/luna_bot counts the number of times Luna is used in pet subreddits")
aww = set()

for i in xrange(0,25)
    comments = r.get_comments('aww')
    for comment in comments:
        body = comment.body.lower()
        if body.find("luna"):
            aww.add(comment.author) 
    time.sleep(60) #Sleep for 1 minute
