import sys
import argparse
from twython import Twython
import requests
import json
import random
import time
import keys

parser = argparse.ArgumentParser(description='Send out tweets whenever your team is on a power play!')
parser.add_argument(
    'team',
    help='The team you want to monitor for a power play. (e.g. Vegas Golden  Knights)',
    type=str
)
parser.add_argument(
    '-i, --i',
    help='File containting tweets you want to send when your team is on the power play.'
)
args = parser.parse_args()


#nhl_games_api = "https://statsapi.web.nhl.com/api/v1/teams/TEAM"
#nhl_teams_api = "https://statsapi.web.nhl.com/api/v1/teams/TEAM"
#nhl_live_api = "https://statsapi.web.nhl.com/api/v1/game/GAME/linescore"

