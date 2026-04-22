user_profile = {
    "favorite_genres": ["lofi", "ambient", "jazz", "folk"],
    "favorite_moods": ["chill", "focused", "relaxed", "peaceful"],
   
    "energy_range": (0.2, 0.5),       # Low to mid intensity
    "valence_range": (0.4, 0.8),      # Neutral to very positive
    "acousticness_range": (0.7, 1.0), # High preference for organic sounds
    "danceability_range": (0.3, 0.7), # Moderate rhythm stability
    
    "target_tempo": 80
}

# main.py or testing_suite.py

# Profile 1: The Conflicting Vibe (The "Aggressive Crying" Test)
# Tests if high weights for 'dark/moody' labels override very high energy scores.
conflicting_vibe = {
    "favorite_genres": ["metal", "rock"],
    "favorite_moods": ["dark", "moody"],
    "target_energy": 0.10,        # Conflict: Metal/Rock is usually > 0.8 energy
    "target_valence": 0.90,       # Conflict: Dark/Moody usually has low valence
    "target_acousticness": 0.90,   # Conflict: Metal is rarely acoustic
    "target_danceability": 0.10
}

# Profile 2: The Ghost User (The "Empty Preference" Test)
# Tests if the system crashes or successfully falls back to numerical proximity 
# when categorical bonuses (Genre/Mood) are zero.
ghost_user = {
    "favorite_genres": [],        # Empty list
    "favorite_moods": [],         # Empty list
    "target_energy": 0.50,
    "target_valence": 0.50,
    "target_acousticness": 0.50,
    "target_danceability": 0.50
}

# Profile 3: The Extreme Polar (The "Impossible Match" Test)
# Tests if the algorithm can find a "closest fit" when values are at absolute 
# opposites (0.0 vs 1.0) compared to the catalog's typical distribution.
extreme_polar = {
    "favorite_genres": ["classical"], # Usually low energy/high acoustic
    "favorite_moods": ["peaceful"],
    "target_energy": 1.0,             # Absolute opposite of genre typicality
    "target_valence": 0.0,            # Absolute opposite of mood typicality
    "target_acousticness": 0.0,
    "target_danceability": 1.0
}