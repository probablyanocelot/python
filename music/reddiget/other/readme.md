INCREASE STREAM SPEED BY REPLACING youtube.py in site-packages/youtube-dl/extractor/ with:
https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-956200172


Solution for playlist creation by using Reddit API to scrape urls subreddits.

--- FLOW ---

• run.py • reddibot.py : Collect video/(maybe audio) urls using Reddit API, write to JSON • jukebot.py : Collect urls from JSON, play them in a loop

!!! REQUIREMENTS !!!

    Download VLC media player (ensure correct architecture x64/x86)

    Enable your Reddit account to use Reddit API by visiting: https://www.reddit.com/prefs/apps/ step-by-step: https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c

    Use 'pipenv --install' in project directory to install python dependencies

NOTES:

*   supposed to run reddibot.py in order to get 'data.json', BUT
        pre-made data.json will be included for testing purposes.

**  careful using Reddit API, as it is limited to 60 requests per minute.
        files utilizing this include run.py and reddibot.py

*** CREATE .env FILE WITH CREDENTIALS FOR reddibot.py; <- dev note: create instructions for this
