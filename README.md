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
    2. If you have not already:
        1. Create a personal use script app [here](https://www.reddit.com/prefs/apps)
        2. Read the terms of service and register your app [here](https://docs.google.com/a/reddit.com/forms/d/1ao_gme8e_xfZ41q4QymFqg5HD29HggOD8I9-MFTG7So/viewform)
    2. Fill in the appropriate values immediatly after each equals (=) sign

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
