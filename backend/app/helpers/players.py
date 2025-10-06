import json
import os
import random
from collections import defaultdict

from app.dbmodels import models

def get_player_summary_stats(player_id: str):
    """
    Get player summary statistics from the database.
    
    Args:
        player_id (str): The player ID to get stats for
        
    Returns:
        dict: Player summary statistics matching the expected format
    """
    try:
        player = models.Player.objects.get(player_id=int(player_id))
    except models.Player.DoesNotExist:
        return {}
    
    # Get all shots for the player
    shots = models.Shot.objects.filter(player=player)
    
    # Get all passes for the player
    passes = models.Pass.objects.filter(player=player)
    
    # Get all turnovers for the player
    turnovers = models.Turnover.objects.filter(player=player)
    
    # Calculate totals
    total_shot_attempts = shots.count()
    total_points = sum(shot.points for shot in shots)
    total_passes = passes.count()
    total_potential_assists = passes.filter(potential_assist=True).count()
    total_turnovers = turnovers.count()
    total_passing_turnovers = passes.filter(turnover=True).count()
    
    # Count actions by type
    action_counts = defaultdict(int)
    for shot in shots:
        action_counts[shot.action_type] += 1
    for pass_obj in passes:
        action_counts[pass_obj.action_type] += 1
    for turnover in turnovers:
        action_counts[turnover.action_type] += 1
    
    # Build response structure
    response = {
        "name": player.name,
        "playerID": player.player_id,
        "totalShotAttempts": total_shot_attempts,
        "totalPoints": total_points,
        "totalPasses": total_passes,
        "totalPotentialAssists": total_potential_assists,
        "totalTurnovers": total_turnovers,
        "totalPassingTurnovers": total_passing_turnovers,
        "pickAndRollCount": action_counts['pickAndRoll'],
        "isolationCount": action_counts['isolation'],
        "postUpCount": action_counts['postUp'],
        "offBallScreenCount": action_counts['offBallScreen'],
    }
    
    # Build action-specific data
    action_types = ['pickAndRoll', 'isolation', 'postUp', 'offBallScreen']
    
    for action_type in action_types:
        action_shots = shots.filter(action_type=action_type)
        action_passes = passes.filter(action_type=action_type)
        action_turnovers = turnovers.filter(action_type=action_type)
        
        action_shot_attempts = action_shots.count()
        action_points = sum(shot.points for shot in action_shots)
        action_passes_count = action_passes.count()
        action_potential_assists = action_passes.filter(potential_assist=True).count()
        action_turnovers_count = action_turnovers.count()
        action_passing_turnovers = action_passes.filter(turnover=True).count()
        
        # Build shots list for this action type
        action_shots_list = [
            {
                "loc": [shot.shot_loc_x, shot.shot_loc_y],
                "points": shot.points
            }
            for shot in action_shots
        ]
        
        # Build passes list for this action type
        action_passes_list = [
            {
                "startLoc": [pass_obj.ball_start_loc_x, pass_obj.ball_start_loc_y],
                "endLoc": [pass_obj.ball_end_loc_x, pass_obj.ball_end_loc_y],
                "isCompleted": pass_obj.completed_pass,
                "isPotentialAssist": pass_obj.potential_assist,
                "isTurnover": pass_obj.turnover
            }
            for pass_obj in action_passes
        ]
        
        # Build turnovers list for this action type
        action_turnovers_list = [
            {
                "loc": [turnover.tov_loc_x, turnover.tov_loc_y]
            }
            for turnover in action_turnovers
        ]
        
        response[action_type] = {
            "totalShotAttempts": action_shot_attempts,
            "totalPoints": action_points,
            "totalPasses": action_passes_count,
            "totalPotentialAssists": action_potential_assists,
            "totalTurnovers": action_turnovers_count,
            "totalPassingTurnovers": action_passing_turnovers,
            "shots": action_shots_list,
            "passes": action_passes_list,
            "turnovers": action_turnovers_list
        }
    
    return response


def get_ranks(player_id: str, player_summary: dict):
    """
    Calculate player rankings against all players for various statistics.
    
    Args:
        player_id (str): The player ID to calculate ranks for
        player_summary (dict): The player's summary statistics
        
    Returns:
        dict: Rankings for each statistic
    """
    if not player_summary:
        return {}
    
    # Get all players' stats for comparison
    all_players = models.Player.objects.all()
    
    # Calculate totals for all players
    all_stats = {}
    for player in all_players:
        shots = models.Shot.objects.filter(player=player)
        passes = models.Pass.objects.filter(player=player)
        turnovers = models.Turnover.objects.filter(player=player)
        
        # Count actions by type
        action_counts = defaultdict(int)
        for shot in shots:
            action_counts[shot.action_type] += 1
        for pass_obj in passes:
            action_counts[pass_obj.action_type] += 1
        for turnover in turnovers:
            action_counts[turnover.action_type] += 1
        
        all_stats[player.player_id] = {
            'totalShotAttempts': shots.count(),
            'totalPoints': sum(shot.points for shot in shots),
            'totalPasses': passes.count(),
            'totalPotentialAssists': passes.filter(potential_assist=True).count(),
            'totalTurnovers': turnovers.count(),
            'totalPassingTurnovers': passes.filter(turnover=True).count(),
            'pickAndRollCount': action_counts['pickAndRoll'],
            'isolationCount': action_counts['isolation'],
            'postUpCount': action_counts['postUp'],
            'offBallScreenCount': action_counts['offBallScreen'],
        }
    
    # Calculate ranks (lower is better for turnovers, higher is better for others)
    stats_to_rank = [
        'totalShotAttempts', 'totalPoints', 'totalPasses', 'totalPotentialAssists',
        'totalTurnovers', 'totalPassingTurnovers', 'pickAndRollCount', 
        'isolationCount', 'postUpCount', 'offBallScreenCount'
    ]
    
    ranks = {}
    current_player_id = int(player_id)
    
    for stat in stats_to_rank:
        # Get all values for this stat
        values = [(pid, all_stats[pid][stat]) for pid in all_stats.keys()]
        
        # Sort by value (descending for most stats, ascending for turnovers)
        reverse_sort = stat not in ['totalTurnovers', 'totalPassingTurnovers']
        values.sort(key=lambda x: x[1], reverse=reverse_sort)
        
        # Find rank (1-based)
        for rank, (pid, value) in enumerate(values, 1):
            if pid == current_player_id:
                rank_key = f"{stat}Rank"
                ranks[rank_key] = rank
                break
    
    return ranks
