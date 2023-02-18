from nba_api.stats.endpoints import teamdashboardbygeneralsplits
from nba_api.stats import Endpoint

team_list = Endpoint.team_list().get_data()
for team in team_list:
    team_id = team['id']
    team_name = team['full_name']
    team_info = Endpoint.team_summary(team_id).get_data()[0]
    offrtg = team_info['off_rtg']
    defrtg = team_info['def_rtg']
    print(f"Team name: {team_name}")
    print(f"Offensive rating: {offrtg}")
    print(f"Defensive rating: {defrtg}")

