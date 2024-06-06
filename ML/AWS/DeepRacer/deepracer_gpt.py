def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    is_offtrack = params['is_offtrack']
    
    # Calculate 3 marks that are farther and farther away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give a higher reward if the car is closer to the center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Additional reward if all four wheels are on the track
    if all_wheels_on_track:
        reward += 0.5

    # Penalize if the car goes off track
    if is_offtrack:
        reward = 1e-3

    # Reward for speed
    SPEED_THRESHOLD = 1.0
    if speed > SPEED_THRESHOLD:
        reward += 0.5

    # Reward for progress
    if progress > 75:
        reward += 10.0

    # Encourage the car to complete the track faster with fewer steps
    if steps > 0:
        reward += (progress / steps) * 100

    return float(reward)
