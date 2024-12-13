
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players
from typing import Dict, Union

def fetch_player_stats(player_name: str) -> Dict[str, Union[str, float]]:
    """
    Fetch NBA player stats from the NBA API.

    Args:
        player_name (str): Full name of the player (first and last name).

    Returns:
        Dict[str, Union[str, float]]: A dictionary containing the player's stats or an error message.
    """
    # Check if the input is numeric
    if player_name.isnumeric():
        return {"error": "Invalid input: Please enter a valid player's name, not a number."}

    player_info = players.find_players_by_full_name(player_name)

    # Check if no player is found
    if not player_info:
        return {"error": "Player not found! Please check the name."}

    # If multiple players are found (e.g., partial match), return an error
    if len(player_info) > 1:
        return {"error": "Multiple players found. Please enter a first and last name."}

    # Get player ID
    player_id = player_info[0]['id']

    # Fetch player info
    player_info_endpoint = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_info_dict = player_info_endpoint.get_normalized_dict()
    player_summary = player_info_dict["CommonPlayerInfo"][0]

    # Extract team and position
    team = player_summary.get("TEAM_NAME", "N/A")
    position = player_summary.get("POSITION", "N/A")

    # Fetch career stats and calculate averages
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_dict = career_stats.get_normalized_dict()
    latest_season = career_stats_dict["SeasonTotalsRegularSeason"][-1]

    games_played = latest_season.get("GP", 0)
    if games_played > 0:
        ppg = latest_season.get("PTS", 0) / games_played
        rpg = latest_season.get("REB", 0) / games_played
        apg = latest_season.get("AST", 0) / games_played
        bpg = latest_season.get("BLK", 0) / games_played
        spg = latest_season.get("STL", 0) / games_played
        fg_pct = latest_season.get("FG_PCT", 0)
        three_pt_pct = latest_season.get("FG3_PCT", 0)
    else:
        ppg = rpg = apg = bpg = spg = fg_pct = three_pt_pct = 0

    return {
        "team": team,
        "position": position,
        "games_played": games_played,
        "ppg": ppg,
        "rpg": rpg,
        "apg": apg,
        "bpg": bpg,
        "spg": spg,
        "fg_pct": fg_pct,
        "three_pt_pct": three_pt_pct
    }
