import functions
teamid = 54
team = functions.get_team_name(teamid)
game = functions.check_if_playing(teamid)

functions.twitter_loop(team, teamid)
