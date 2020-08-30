import requests
import praw
import tkinter as tk
# import redditapi

def redditAPI(subr, sortby, Limit):
    reddit = praw.Reddit(client_id="XXXXX",#CLIENT ID AND CLIENT SECRET
                        client_secret="XXXXX",#GET FROM REDDIT.COM/PREFS/APPS
                        password="XXXXX",#REDDIT PASSWORD
                        user_agent="XXXXX",#RANDOM KEY CAN BE ANYTHING
                        username="XXXXX")#REDDIT USERNAME
    subreddit = reddit.subreddit(subr)

    if(sortby=="New"): 
        hot_python = subreddit.new(limit=Limit)
    if (sortby=="Top"): 
        hot_python = subreddit.top(limit=Limit) 
    if (sortby=="Hot"): 
        hot_python = subreddit.hot(limit=Limit)
    
    for submission in hot_python:
        if not submission.stickied:
            print("\n=================")
            print("ANAME: " + str(submission.author.name))
            print("Post karma: " + str(submission.author.link_karma))
            print("Comment Karma: " + str(submission.author.comment_karma))
            print("Title: " + str(submission.title))
            n=0
            j=0

            for sub1 in submission.comments:
                n+=1

            for sub in submission.comments:
                j+=1
                print(f"Comment{j}: " + sub.body)
                if n == j:
                    print("\nLAST COMMENT\n")

            print("\n=================")