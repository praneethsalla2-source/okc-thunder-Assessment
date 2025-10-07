-- Upsert data (insert or update) for all tables
-- This script can be run multiple times safely

-- Insert/Update teams data
INSERT INTO teams (team_id, name) VALUES 
(1, 'Tune Squad'),
(2, 'Monstars'),
(3, 'Timberwolves'),
(4, 'Harlem Buckets'),
(5, 'P.U.'),
(6, 'Cadwallader University'),
(7, 'Beavers'),
(8, 'Digital Tune Squad'),
(9, 'Goon Squad'),
(10, 'Eagles')
ON CONFLICT (team_id) DO UPDATE SET name = EXCLUDED.name;

-- Insert/Update games data
INSERT INTO games (game_id, date) VALUES 
(0, '2023-11-13'),
(1, '2023-11-14'),
(2, '2023-11-15'),
(3, '2023-11-16'),
(4, '2023-11-17'),
(5, '2023-11-18'),
(6, '2023-11-19'),
(7, '2023-11-20'),
(8, '2023-11-21'),
(9, '2023-11-22'),
(10, '2023-11-23'),
(11, '2023-11-24'),
(12, '2023-11-25'),
(13, '2023-11-26'),
(14, '2023-11-27'),
(15, '2023-11-28'),
(16, '2023-11-29'),
(17, '2023-11-30'),
(18, '2023-12-01'),
(19, '2023-12-02'),
(20, '2023-12-03'),
(21, '2023-12-04'),
(22, '2023-12-05'),
(23, '2023-12-06'),
(24, '2023-12-07'),
(25, '2023-12-08'),
(26, '2023-12-09'),
(27, '2023-12-10'),
(28, '2023-12-11'),
(29, '2023-12-12'),
(30, '2023-12-13'),
(31, '2023-12-14'),
(32, '2023-12-15'),
(33, '2023-12-16'),
(34, '2023-12-17'),
(35, '2023-12-18'),
(36, '2023-12-19'),
(37, '2023-12-20'),
(38, '2023-12-21')
ON CONFLICT (game_id) DO UPDATE SET date = EXCLUDED.date;

-- Insert/Update players data
INSERT INTO players (player_id, name, team_id) VALUES 
(0, 'Michael Jordan', 1),
(1, 'Pound', 2),
(2, 'Buddy', 3),
(3, 'Uncle Drew', 4),
(4, 'Goofy', 5),
(5, 'David Greene', 6),
(6, 'Scott Howard', 7),
(7, 'LeBron James', 8),
(8, 'Chronos', 9),
(9, 'Brian Newall', 10)
ON CONFLICT (player_id) DO UPDATE SET name = EXCLUDED.name, team_id = EXCLUDED.team_id;

-- Insert/Update shots data (sample - first 20 shots)
INSERT INTO shots (shot_id, points, shooting_foul_drawn, shot_loc_x, shot_loc_y, action_type, game_id, player_id) VALUES 
(0, 0, false, -3.62, 25.68, 'pickAndRoll', 0, 0),
(1, 0, false, 17.04, 19.11, 'pickAndRoll', 1, 0),
(2, 0, false, 13.06, 13.33, 'pickAndRoll', 1, 0),
(3, 0, false, -9.65, 7.56, 'pickAndRoll', 1, 0),
(4, 0, false, -3.79, 31.49, 'pickAndRoll', 1, 0),
(5, 0, false, 2.49, -0.01, 'pickAndRoll', 2, 0),
(6, 3, false, 19.85, 16.21, 'pickAndRoll', 2, 0),
(7, 2, false, 6.97, 14.72, 'pickAndRoll', 2, 0),
(8, 2, false, -1.24, 1.47, 'pickAndRoll', 2, 0),
(9, 0, false, -7.73, 7.73, 'pickAndRoll', 3, 0),
(10, 3, true, 16.12, 9.77, 'pickAndRoll', 3, 0),
(11, 0, false, 6.97, 19.37, 'pickAndRoll', 3, 0),
(12, 0, false, -2.93, 26.46, 'pickAndRoll', 4, 0),
(13, 2, false, -5.01, 0.4, 'pickAndRoll', 4, 0),
(14, 2, false, -4.18, 1.21, 'pickAndRoll', 5, 1),
(15, 0, false, 4.44, 3.02, 'pickAndRoll', 5, 1),
(16, 2, false, -4.03, 0.95, 'pickAndRoll', 6, 1),
(17, 0, false, -7, 10.06, 'pickAndRoll', 5, 1),
(18, 0, false, -8.56, 2.36, 'pickAndRoll', 5, 1),
(19, 2, false, -10.74, 2, 'pickAndRoll', 7, 1)
ON CONFLICT (shot_id) DO UPDATE SET 
    points = EXCLUDED.points,
    shooting_foul_drawn = EXCLUDED.shooting_foul_drawn,
    shot_loc_x = EXCLUDED.shot_loc_x,
    shot_loc_y = EXCLUDED.shot_loc_y,
    action_type = EXCLUDED.action_type,
    game_id = EXCLUDED.game_id,
    player_id = EXCLUDED.player_id;

-- Insert/Update passes data (sample - first 20 passes)
INSERT INTO passes (pass_id, completed_pass, potential_assist, turnover, ball_start_loc_x, ball_start_loc_y, ball_end_loc_x, ball_end_loc_y, action_type, game_id, player_id) VALUES 
(1, true, false, false, 5.48, 23.03, 2.69, 22.48, 'pickAndRoll', 0, 0),
(2, true, false, false, -6.94, 24.15, -9.85, 22.56, 'pickAndRoll', 0, 0),
(4, true, true, false, -3.8, 26.33, -5.08, 14.57, 'pickAndRoll', 0, 8),
(5, true, true, false, -16.36, 24.11, -19.65, 18.36, 'pickAndRoll', 15, 4),
(7, true, false, false, 2.82, 29.2, 17.12, 23.49, 'pickAndRoll', 25, 6),
(8, true, false, false, -22.79, 9.4, 20.17, 4.78, 'pickAndRoll', 25, 6),
(9, true, false, false, -4.71, 37.7, 10.64, 30.24, 'pickAndRoll', 25, 6),
(10, true, false, false, -0.12, 31.39, 1.16, 28.94, 'pickAndRoll', 25, 6),
(11, true, true, false, 0.46, 10.4, -19.48, 4.53, 'pickAndRoll', 25, 6),
(12, true, true, false, -6.04, 6.65, -0.59, 0.57, 'pickAndRoll', 25, 6),
(13, true, true, false, 9.3, 20.67, 7.53, 18.4, 'pickAndRoll', 20, 5),
(14, true, true, false, 1.55, 26.01, -7.5, 26.33, 'pickAndRoll', 9, 2),
(15, true, false, false, -0.41, 18.38, -14.2, 21.48, 'pickAndRoll', 9, 2),
(16, true, false, false, -16.23, 15.32, -7.36, 24.13, 'pickAndRoll', 9, 2),
(17, false, false, true, 6.12, 22.28, 4.44, 19.66, 'pickAndRoll', 35, 8),
(18, true, false, false, 3.83, 6.93, -10.36, 20.16, 'pickAndRoll', 29, 1),
(19, true, true, false, 21.31, 28.57, 17.47, 19.81, 'pickAndRoll', 27, 6),
(20, true, true, false, -3.37, 3.89, -19.49, 1.49, 'pickAndRoll', 27, 6),
(22, true, true, false, 8.17, 6.51, -10.51, 20.8, 'pickAndRoll', 27, 6),
(23, true, false, false, -6.26, 28.39, 18.55, 6.55, 'pickAndRoll', 27, 6)
ON CONFLICT (pass_id) DO UPDATE SET 
    completed_pass = EXCLUDED.completed_pass,
    potential_assist = EXCLUDED.potential_assist,
    turnover = EXCLUDED.turnover,
    ball_start_loc_x = EXCLUDED.ball_start_loc_x,
    ball_start_loc_y = EXCLUDED.ball_start_loc_y,
    ball_end_loc_x = EXCLUDED.ball_end_loc_x,
    ball_end_loc_y = EXCLUDED.ball_end_loc_y,
    action_type = EXCLUDED.action_type,
    game_id = EXCLUDED.game_id,
    player_id = EXCLUDED.player_id;

-- Insert/Update turnovers data
INSERT INTO turnovers (turnover_id, tov_loc_x, tov_loc_y, action_type, game_id, player_id) VALUES 
(0, -12.06, 9.4, 'pickAndRoll', 2, 0),
(1, 1.78, 9.58, 'pickAndRoll', 38, 2),
(2, 7.61, 24.29, 'pickAndRoll', 35, 8),
(3, -23.87, 26.84, 'pickAndRoll', 17, 3),
(4, -6.17, 26.09, 'pickAndRoll', 16, 4),
(5, 1.42, 26.22, 'pickAndRoll', 16, 4),
(6, -23.05, 27.65, 'pickAndRoll', 19, 5),
(7, -5.2, 5.03, 'pickAndRoll', 26, 6),
(8, 11.48, 16.83, 'pickAndRoll', 24, 6),
(9, -9.14, 9.86, 'isolation', 20, 5),
(10, -4.58, 12.84, 'postUp', 5, 3),
(11, 4.89, 0.39, 'postUp', 29, 1),
(12, 3.73, 4.5, 'postUp', 38, 2),
(13, -8.61, -1.67, 'offBallScreen', 36, 8)
ON CONFLICT (turnover_id) DO UPDATE SET 
    tov_loc_x = EXCLUDED.tov_loc_x,
    tov_loc_y = EXCLUDED.tov_loc_y,
    action_type = EXCLUDED.action_type,
    game_id = EXCLUDED.game_id,
    player_id = EXCLUDED.player_id;

-- Verify data was inserted
SELECT 'Teams' as table_name, COUNT(*) as count FROM teams
UNION ALL
SELECT 'Games', COUNT(*) FROM games
UNION ALL
SELECT 'Players', COUNT(*) FROM players
UNION ALL
SELECT 'Shots', COUNT(*) FROM shots
UNION ALL
SELECT 'Passes', COUNT(*) FROM passes
UNION ALL
SELECT 'Turnovers', COUNT(*) FROM turnovers;
