import praw
import time
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Reddit API credentials from .env
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

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

# Loops through upvoted posts
for submission in upvoted:
    try:
        logger.info(f"Un-upvoting: {submission.title}")
        submission.clear_vote()
        time.sleep(1)  # Sleeps to avoid rate-limit errors
    except Exception as e:
        logger.error(f"Failed to un-upvote {submission.title}: {e}")
        time.sleep(5)  # Longer delay on error

logger.info("All upvoted posts have been un-upvoted!")
