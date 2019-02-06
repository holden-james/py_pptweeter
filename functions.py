import twython
import requests
import json
import random
import time
import keys

# Given the team's name and link to the NHL api, find the team's ID.


def get_team_id(team, api):
    request = requests.get(url=api)
    result = json.loads(request.text)

    index = 0
    while result['teams'][index]['name'] != team:
        index += 1

    return result['teams'][index]['id']


def check_if_playing(team, api):
    request = requests.get(url=api)
    result = json.loads(request.text)
    try:
        games_today = result["dates"][0]["games"][0]["gamePk"]
    except IndexError:
        print(f"The {team} are not playing a game today... Goodbye.")
        quit()
    return games_today

# Using the game's ID, check if the team is on a a power play.
# Checks are run against the NHL's API for the live game.


def check_power_play(teamid, team):
    game = check_if_playing(teamid)
    api = f"https://statsapi.web.nhl.com/api/v1/game/{game}/linescore"
    request = requests.get(url=api)
    result = json.loads(request.text)

    home = result["teams"]["home"]["team"]["name"]
    away = result["teams"]["away"]["team"]["name"]

    if team in home:
        on_power_play = result["teams"]["home"]["powerPlay"]
        return on_power_play
    elif team in away:
        on_power_play = result["teams"]["away"]["powerPlay"]
        return on_power_play

#


def twitter_loop(team, teamid):
    twitter = twython.Twython(
        keys.consumer_key,
        keys.consumer_secret,
        keys.access_token,
        keys.access_token_secret
    )

    while not check_power_play(teamid, get_team_name(teamid)):
        print(f"The {team} are not on a power play...")
        time.sleep(15)
    else:
        tweet_options = [
            "@AdamSKutner Go Knights Go! #AdamKutnerPowerPlay",
            "@AdamSKutner VGK Power Play! #AdamKutnerPowerPlay",
            "@AdamSKutner I believe! #AdamKutnerPowerPlay",
            "@AdamSKutner Let's get that power play goal! #AdamKutnerPowerPlay",
            "@AdamSKutner Let's get it! #AdamKutnerPowerPlay",
            "@AdamSKutner Powerrrrr Playyyyyy! #AdamKutnerPowerPlay"
        ]
        tweet_number = random.randint(0, (len(tweet_options))-1)
        message = tweet_options[tweet_number]
        print("Tweeting this message: " + message)
        twitter.update_status(status=message)
        print(f"The {team} are on a power play!")
        print("Waiting five minutes to start the loop again...")
        time.sleep(300)
        twitter_loop()
