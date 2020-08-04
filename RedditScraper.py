import praw
import pandas as pd

redditApp = praw.Reddit(client_id='XDVRjPR6Wnr1ig', client_secret='crfLIN0aF9eGnmefzjzcW6hmcw4', user_agent='RedditScraping')

top_posts = redditApp.subreddit('InternetIsBeautiful').top(limit=1000) #top 1k post on the subreddit
posts = []


for post in top_posts:
    posts.append([post.title, post.score, post.id, post.url])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'url'])


posts.to_csv('top.csv')
