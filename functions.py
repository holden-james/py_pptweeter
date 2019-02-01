import requests
import json


def get_team_name(teamid):
    api = f"https://statsapi.web.nhl.com/api/v1/teams/{teamid}"
    request = requests.get(url=api)
    result = json.loads(request.text)
    team_name = result["teams"][0]["name"]
    return team_name


def check_if_playing(teamid):
    team = get_team_name(teamid)
    api = f"https://statsapi.web.nhl.com/api/v1/schedule?teamId={teamid}"
    request = requests.get(url=api)
    result = json.loads(request.text)
    try:
        games_today = result["dates"][0]["games"][0]["gamePk"]
    except IndexError:
        print(f"The {team} are not playing today...")
        quit()
    return games_today


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
