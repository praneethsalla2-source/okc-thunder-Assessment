#!/usr/bin/env python3
"""
Data loading script for basketball analytics application.
This script loads the raw JSON data into the normalized PostgreSQL database.
"""

import os
import sys
import json
import django
from datetime import datetime
from django.db import transaction

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from app.dbmodels.models import Team, Game, Player, Shot, Pass, Turnover


def load_teams():
    """Load teams data from JSON file"""
    print("Loading teams...")
    teams_path = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'teams.json')
    
    with open(teams_path, 'r') as f:
        teams_data = json.load(f)
    
    teams_created = 0
    for team_data in teams_data:
        team, created = Team.objects.get_or_create(
            team_id=team_data['team_id'],
            defaults={'name': team_data['name']}
        )
        if created:
            teams_created += 1
    
    print(f"Teams loaded: {teams_created} new teams created")
    return teams_created


def load_games():
    """Load games data from JSON file"""
    print("Loading games...")
    games_path = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'games.json')
    
    with open(games_path, 'r') as f:
        games_data = json.load(f)
    
    games_created = 0
    for game_data in games_data:
        game_date = datetime.strptime(game_data['date'], '%Y-%m-%d').date()
        game, created = Game.objects.get_or_create(
            game_id=game_data['id'],
            defaults={'date': game_date}
        )
        if created:
            games_created += 1
    
    print(f"Games loaded: {games_created} new games created")
    return games_created


def load_players():
    """Load players data from JSON file"""
    print("Loading players...")
    players_path = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'players.json')
    
    with open(players_path, 'r') as f:
        players_data = json.load(f)
    
    players_created = 0
    for player_data in players_data:
        team = Team.objects.get(team_id=player_data['team_id'])
        player, created = Player.objects.get_or_create(
            player_id=player_data['player_id'],
            defaults={
                'name': player_data['name'],
                'team': team
            }
        )
        if created:
            players_created += 1
    
    print(f"Players loaded: {players_created} new players created")
    return players_created


def load_shots():
    """Load shots data from players JSON file"""
    print("Loading shots...")
    players_path = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'players.json')
    
    with open(players_path, 'r') as f:
        players_data = json.load(f)
    
    shots_created = 0
    for player_data in players_data:
        player = Player.objects.get(player_id=player_data['player_id'])
        
        for shot_data in player_data.get('shots', []):
            game = Game.objects.get(game_id=shot_data['game_id'])
            shot, created = Shot.objects.get_or_create(
                shot_id=shot_data['id'],
                defaults={
                    'player': player,
                    'game': game,
                    'points': shot_data['points'],
                    'shooting_foul_drawn': shot_data['shooting_foul_drawn'],
                    'shot_loc_x': shot_data['shot_loc_x'],
                    'shot_loc_y': shot_data['shot_loc_y'],
                    'action_type': shot_data['action_type']
                }
            )
            if created:
                shots_created += 1
    
    print(f"Shots loaded: {shots_created} new shots created")
    return shots_created


def load_passes():
    """Load passes data from players JSON file"""
    print("Loading passes...")
    players_path = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'players.json')
    
    with open(players_path, 'r') as f:
        players_data = json.load(f)
    
    passes_created = 0
    for player_data in players_data:
        player = Player.objects.get(player_id=player_data['player_id'])
        
        for pass_data in player_data.get('passes', []):
            game = Game.objects.get(game_id=pass_data['game_id'])
            pass_obj, created = Pass.objects.get_or_create(
                pass_id=pass_data['id'],
                defaults={
                    'player': player,
                    'game': game,
                    'completed_pass': pass_data['completed_pass'],
                    'potential_assist': pass_data['potential_assist'],
                    'turnover': pass_data['turnover'],
                    'ball_start_loc_x': pass_data['ball_start_loc_x'],
                    'ball_start_loc_y': pass_data['ball_start_loc_y'],
                    'ball_end_loc_x': pass_data['ball_end_loc_x'],
                    'ball_end_loc_y': pass_data['ball_end_loc_y'],
                    'action_type': pass_data['action_type']
                }
            )
            if created:
                passes_created += 1
    
    print(f"Passes loaded: {passes_created} new passes created")
    return passes_created


def load_turnovers():
    """Load turnovers data from players JSON file"""
    print("Loading turnovers...")
    players_path = os.path.join(os.path.dirname(__file__), '..', 'raw_data', 'players.json')
    
    with open(players_path, 'r') as f:
        players_data = json.load(f)
    
    turnovers_created = 0
    for player_data in players_data:
        player = Player.objects.get(player_id=player_data['player_id'])
        
        for turnover_data in player_data.get('turnovers', []):
            game = Game.objects.get(game_id=turnover_data['game_id'])
            turnover, created = Turnover.objects.get_or_create(
                turnover_id=turnover_data['id'],
                defaults={
                    'player': player,
                    'game': game,
                    'tov_loc_x': turnover_data['tov_loc_x'],
                    'tov_loc_y': turnover_data['tov_loc_y'],
                    'action_type': turnover_data['action_type']
                }
            )
            if created:
                turnovers_created += 1
    
    print(f"Turnovers loaded: {turnovers_created} new turnovers created")
    return turnovers_created


def clear_all_data():
    """Clear all existing data from the database"""
    print("Clearing existing data...")
    Turnover.objects.all().delete()
    Pass.objects.all().delete()
    Shot.objects.all().delete()
    Player.objects.all().delete()
    Game.objects.all().delete()
    Team.objects.all().delete()
    print("All existing data cleared")


def main():
    """Main function to load all data"""
    print("Starting data loading process...")
    
    try:
        with transaction.atomic():
            # Clear existing data to avoid duplicates
            clear_all_data()
            
            # Load data in order of dependencies
            teams_created = load_teams()
            games_created = load_games()
            players_created = load_players()
            shots_created = load_shots()
            passes_created = load_passes()
            turnovers_created = load_turnovers()
            
            print("\nData loading completed successfully!")
            print(f"Summary:")
            print(f"  Teams: {teams_created} created")
            print(f"  Games: {games_created} created")
            print(f"  Players: {players_created} created")
            print(f"  Shots: {shots_created} created")
            print(f"  Passes: {passes_created} created")
            print(f"  Turnovers: {turnovers_created} created")
            
    except Exception as e:
        print(f"Error during data loading: {e}")
        raise


if __name__ == '__main__':
    main()


