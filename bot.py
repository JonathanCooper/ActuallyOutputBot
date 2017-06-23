import praw
import config

bot = praw.Reddit(user_agent='ActuallyOutputBot',
	client_id=config.client_id,
    client_secret=config.client_secret,
    username=config.username,
    password=config.password)

subreddit = bot.subreddit('Guitar')
comments = subreddit.stream.comments()

reply_msg = 'Actually, I think you mean "output jack".'

for comment in comments:
	text = comment.body
	if 'input jack' in text.lower():
		comment.reply(reply_msg)
