import sys
import argparse
from twython import Twython
import requests
import json
import random
import time
import keys
import functions

nhl_games_api = "https://statsapi.web.nhl.com/api/v1/teams/TEAM"
nhl_teams_api = "https://statsapi.web.nhl.com/api/v1/teams/"
nhl_live_api = "https://statsapi.web.nhl.com/api/v1/game/GAME/linescore"

# Add arguments to be passed to the script when running it.
parser = argparse.ArgumentParser(description='Send out tweets whenever your team is on a power play!')

# Only required argument is the team's name.
parser.add_argument(
    'team',
    help='The team you want to monitor for a power play. (e.g. Vegas Golden  Knights)',
    type=str
)

# Optionally, a text file can be passed to the script that contains different tweets.
parser.add_argument(
    '-tweets',
    help='File containting tweets you want to send when your team is on the power play.'
)

args = vars(parser.parse_args())

# The team passed in from the command line.
nhl_team = args.get('team')

# Check if a text file containing tweets was passed in.
# If no file was passed in, a default string is used.
# Each lines is split into a list.
if args.get('tweets') is None:
    tweets = [f"{nhl_team} are on a power play!", f"I hope the {nhl_team} score on this power play!"]
else:
    with open(args.get('tweets'), 'r') as tweets:
        tweets = tweets.read().splitlines()

# Choose a random number to select a random tweet.
tweet = tweets[random.randint(0, (len(tweets)) - 1)]

# Given the team name passed in, search the NHL's API to find the team's ID.
try:
    nhl_team_id = functions.get_team_id(nhl_team, nhl_teams_api)

except IndexError:
    print("Team doesn't exist! Make sure you're entering the team's full name (e.g. \"Vegas Golden Knights\")")
