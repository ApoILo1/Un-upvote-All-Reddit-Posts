import praw
import time
import logging

# Reddit API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"
user_agent = "your_user_agent"
username = "your_reddit_username"
password = "your_reddit_password"

# "Login" with Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


user = reddit.user.me()
upvoted = user.upvoted(limit=None)  

# Loops though up-voted posts
for submission in upvoted:
    try:
        logger.info(f"Un-upvoting: {submission.title}")
        submission.clear_vote()
        time.sleep(1)  # Sleeps so that it does not cause a rate-limit error
    except Exception as e:
        logger.error(f"Failed to un-upvote {submission.title}: {e}")
        time.sleep(5)  # Longer delay on error to avoid repeated issues

logger.info("All upvoted posts have been un-upvoted!")
