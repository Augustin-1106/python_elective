team_data = {}

while True:
    team_name = input("Enter team name (or 'q' to quit): ")
    if team_name == 'q':
        break
    
    wins = int(input("Enter number of wins: "))
    losses = int(input("Enter number of losses: "))
    
    team_data[team_name] = [wins, losses]

print("Names of all teams:")
for team_name in team_data.keys():
    print(team_name)

team_with_highest_wins = max(team_data, key=lambda x: team_data[x][0])
print("Team with highest wins:", team_with_highest_wins)

team_with_highest_losses = max(team_data, key=lambda x: team_data[x][1])
print("Team with highest losses:", team_with_highest_losses)

team_name = input("Enter team name to get win percentage: ")
if team_name in team_data:
    wins, losses = team_data[team_name]
    win_percentage = (wins / (wins + losses)) * 100
    print(f"{team_name} win percentage: {win_percentage}%")
else:
    print("Team not found in the dictionary.")