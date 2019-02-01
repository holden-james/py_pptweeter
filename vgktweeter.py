import twython
import random
import time
import functions
import keys

twitter = twython.Twython(
    keys.consumer_key,
    keys.consumer_secret,
    keys.access_token,
    keys.access_token_secret
)

teamid = 54
team = functions.get_team_name(teamid)
game = functions.check_if_playing(teamid)


def twitter_loop():
    while not functions.check_power_play(teamid, functions.get_team_name(teamid)):
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
        tweet_number = random.randint(0, len(tweet_options))
        message = tweet_options[tweet_number]
        print("Tweeting this message: " + message)
        twitter.update_status(status=message)
        print(f"The {team} are on a power play!")
        print("Waiting five minutes to start the loop again...")
        time.sleep(300)


twitter_loop()
