from twython import Twython
import argparse
import random
import time
import keys
import functions
from spinner import Spinner


def twitter_loop(team):
    twitter = Twython(
        keys.consumer_key,
        keys.consumer_secret,
        keys.access_token,
        keys.access_token_secret
    )

    spinner = Spinner()

    print(f"Waiting for {team} to go on a Power Play...", end='')
    spinner.start()

    while not functions.check_power_play(nhl_team, nhl_live_api):
        time.sleep(10)
    else:
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

        spinner.stop()
        print(f"The {team} are on a power play!")
        print("Tweeting this message: " + tweet)

        twitter.update_status(status=tweet)
        time.sleep(300)
        twitter_loop()


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

# Define the link to the NHL API for teams.
# Query the get_team_id function for the team's ID for use with other APIs.
nhl_teams_api = "https://statsapi.web.nhl.com/api/v1/teams/"
nhl_team_id = functions.get_team_id(nhl_team, nhl_teams_api)

# Define the link to the NHL API for a team's current day schule. Passing in the team's ID.
# Using the check_if_playing function, get today's game ID for use with other APIs.
nhl_games_api = f"https://statsapi.web.nhl.com/api/v1/schedule?teamId={nhl_team_id}"
nhl_game_id = functions.check_if_playing(nhl_team, nhl_games_api)

nhl_live_api = f"https://statsapi.web.nhl.com/api/v1/game/{nhl_game_id}/linescore"
functions.check_power_play(nhl_team, nhl_live_api)

twitter_loop(nhl_team)
