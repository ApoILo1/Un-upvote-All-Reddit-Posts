# Un-upvote-All-Reddit-Posts

This Python script allows users to un-upvote all their previously upvoted Reddit posts using the Reddit API (PRAW - Python Reddit API Wrapper). 

## Features
- Automatically un-upvotes all posts you’ve upvoted on Reddit.
- Handles rate limiting to avoid API issues.
- Logs the process of un-upvoting posts.

## Prerequisites
- Python 3.7 or higher
- Reddit account and API credentials (Client ID, Client Secret, etc.)
- PRAW (Python Reddit API Wrapper)

## Installation Guide

### 1. Clone the Repository
To clone this project to your local machine, run the following command:

```bash
git clone https://github.com/yourusername/Un-upvote-All-Reddit-Posts.git
```

Navigate to the cloned directory:
```bash
cd Un-upvote-All-Reddit-Posts/unvoter
```

### 2. Set Up Reddit API Credentials

1. Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps) and click "Create App" or "Create another app."
2. Select **script** as the app type.
3. Fill in the required fields. You will get a **Client ID**, **Client Secret**, and will use your Reddit username and password for authentication.

### 3. Create a `.env` File

After cloning the repo, create a `.env` file in the **root** of the project (outside of the `unvoter` folder).

```
Un-upvote-All-Reddit-Posts/
├── unvoter/
│   └── unvoter.py
├── .env
├── .gitignore
└── README.md
```

In the `.env` file, add your Reddit API credentials in the following format:

```bash
client_id=your_client_id
client_secret=your_client_secret
username=your_reddit_username
password=your_reddit_password
user_agent=your_user_agent
```

### 4. Install Required Dependencies

Use `pip` to install the required modules:

```bash
pip install praw
```

### 5. Running the Script

Once everything is set up, you can run the script to start un-upvoting your Reddit posts:

```bash
cd unvoter
python unvoter.py
```

### Important Notes:
- The script has built-in rate limiting using `time.sleep()` to avoid API errors, please do not remove them.
- It may take multiple runs to un-upvote all posts due to Reddit's rate limiting.

## Troubleshooting

- **OAuth issues**: Ensure your credentials in the `.env` file are correct. Double-check the **Client ID**, **Client Secret**, **Username**, and **Password** fields.
- **Rate limit errors**: The script includes delays between requests to avoid hitting Reddit’s API rate limits, but if you see rate-limit errors, try increasing the delay by modifying the `time.sleep()` values in the script.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
