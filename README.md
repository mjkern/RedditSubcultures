# SubReddit Culture Analysis
The goal is to download the contents of Reddit Subs, analyze the contributors, and study the results.

## Setup

1. Install dependencies
```
$ pip install -r requirements.txt
```

2. Setup Configuration
    1. Create a praw.ini file (from the template)
    ```
    $ cp praw.ini.template praw.ini
    ```
    2. Fill in the appropriate values immediatly after each eqauls (=) sign

3. Verify setup works by running the test.py file. Expected output it 10 large integers,
one per line.
```
$ python test.py
```

## Download Subreddit Content

1. [Optional] Customize configuration by setting `limit` and/or `subreddit_name` in `downloader.py`
2. Run the downloader
```
$ python downloader.py
```
