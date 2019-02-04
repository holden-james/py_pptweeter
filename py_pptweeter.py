import functions

# Define the team ID. Taken from NHL.com's API.
teamid = 54

# Given the team's ID, find their name.
team = functions.get_team_name(teamid)

# Find out if the team is playing today. If they are, assign the game's ID to game.
game = functions.check_if_playing(teamid)

# Run the loop
functions.twitter_loop(team, teamid)
