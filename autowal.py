import praw ##wrapper used to communicate with reddit
import os ##requried for wal and wget

reddit = praw.Reddit(client_id='',                    ##Check https://praw.readthedocs.io/en/latest/getting_started/quick_start.html for info on how to obtain these values
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

subreddit = reddit.subreddit('wallpapers') ##subbredit to use


for submission in subreddit.hot(limit=1): ## gets first submission in hot
    os.system("wget " +  submission.url + " -O wallpaper") ##downloads submission image adn renames it to wallpaper
    os.system("wal -c -i wallpaper") ##sets wallpaper, using -c as wal thinks wallpaper is the same as last wallpaper as they use the same name
