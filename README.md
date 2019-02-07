# py_pptweeter
Tweet something whenever your favorite team goes on the Power Play!

Requires Twython
```
pip3 install Twython
```


File keys.py must be created in root folder. Define the following variables in **keys.py**:
```
consumer_key = 'KEY'
consumer_secret = 'SECRET'
access_token = 'TOKEN'
access_token_secret = 'SECRET'
```

How to run the script:
```
python pptweeter.py "NHL TEAM NAME"
```

NHL Team Name needs to be the full team (e.g. "Vegas Golden Knights").

By default the script will post one of two generic tweets when the team goes on a power play. Alternatively, point to a .txt file containing tweets using the following:
```
python pptweeter.py "NHL TEAM NAME" -tweets location\of\tweets.txt
```

Make sure each tweet is on a new line in the .txt.
