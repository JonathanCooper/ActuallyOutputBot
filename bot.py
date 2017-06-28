import praw
import config

bot = praw.Reddit(user_agent='ActuallyOutputBot',
    client_id=config.client_id,
    client_secret=config.client_secret,
    username=config.username,
    password=config.password)

subreddit = bot.subreddit('Guitar')
comments = subreddit.stream.comments()

reply_msg = 'I think you mean [output jack](https://en.wikipedia.org/wiki/Electric_guitar#Construction).'

for comment in comments:
    text = comment.body.lower()
    if 'input jack' in text and 'amp' not in text:
        print 'found a match: {0}'.format(comment.permalink())
        comment.reply(reply_msg)
