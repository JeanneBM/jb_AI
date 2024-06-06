'''
def reward_function(params):
    '''
    Example of rewarding the agent to follow an optimal racing line with speed
    for the A to Z Speedway track
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    is_offtrack = params['is_offtrack']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Calculate the optimal racing line reward
    def calculate_optimal_racing_line(waypoints, closest_waypoints):
        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]
        track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
        track_direction = math.degrees(track_direction)
        return track_direction

    # Calculate distance from the racing line
    track_direction = calculate_optimal_racing_line(waypoints, closest_waypoints)
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Calculate markers that are at varying distances from the optimal racing line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give a high reward if the car is within the optimal racing line and maintaining speed
    if distance_from_center <= marker_1 and direction_diff < 10:
        reward = 1.0
    elif distance_from_center <= marker_2 and direction_diff < 15:
        reward = 0.5
    elif distance_from_center <= marker_3 and direction_diff < 20:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Additional reward if all four wheels are on the track
    if all_wheels_on_track:
        reward += 0.5

    # Penalize if the car goes off track
    if is_offtrack:
        reward = 1e-3

    # Reward for speed, encourage higher speeds on straight portions
    SPEED_THRESHOLD = 2.0
    if speed > SPEED_THRESHOLD:
        reward += 1.0

    # Reward for progress and fewer steps
    if steps > 0:
        reward += (progress / steps) * 100

    return float(reward)
'''

import math

def reward_function(params):
    '''
    Reward function for AWS DeepRacer on the A to Z Speedway track
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    is_offtrack = params['is_offtrack']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Calculate the optimal racing line reward
    def calculate_optimal_racing_line(waypoints, closest_waypoints):
        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]
        track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
        track_direction = math.degrees(track_direction)
        return track_direction

    # Calculate distance from the racing line
    track_direction = calculate_optimal_racing_line(waypoints, closest_waypoints)
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Calculate markers that are at varying distances from the optimal racing line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give a high reward if the car is within the optimal racing line and maintaining speed
    if distance_from_center <= marker_1 and direction_diff < 10:
        reward = 1.0
    elif distance_from_center <= marker_2 and direction_diff < 15:
        reward = 0.5
    elif distance_from_center <= marker_3 and direction_diff < 20:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Additional reward if all four wheels are on the track
    if all_wheels_on_track:
        reward += 0.5

    # Penalize if the car goes off track
    if is_offtrack:
        reward = 1e-3

    # Reward for speed, encourage higher speeds on straight portions
    SPEED_THRESHOLD = 2.0
    if speed > SPEED_THRESHOLD:
        reward += 1.0

    # Reward for progress and fewer steps
    if steps > 0:
        reward += (progress / steps) * 100

    return float(reward)

