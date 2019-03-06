import requests
import json
import random

# Given the team's name and link to the NHL api, find the team's NHL ID.
def get_team_id(team, api):
    request = requests.get(url=api)
    result = json.loads(request.text)

    try:
        index = 0
        while result['teams'][index]['name'] != team:
            index += 1
    except IndexError:
        print("Team doesn't exist! Make sure you're entering the team's full name (e.g. \"Vegas Golden Knights\")")
        quit()

    return result['teams'][index]['id']

# Given the team's name and link to the NHL api, find if the team is playing today.
# If the team is playing today, return the NHL's gameid for the game.
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
def check_power_play(team, api):
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

chosen_tweets = []
def choose_tweet(tweets):
    random_number = random.randint(0, (len(tweets)) - 1)
    if random_number not in chosen_tweets:
        chosen_tweets.append(random_number)
        tweet = tweets[random_number]
        return tweet
    else:
        choose_tweet(tweets)
    