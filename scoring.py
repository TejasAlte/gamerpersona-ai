def gaming_intensity(daily_hours, years_gaming, spending):
    score = (daily_hours * 6) + (years_gaming * 2) + (spending / 25)
    return min(score, 100)


def sleep_balance(sleep_hours, sleep_quality):
    score = 100 - abs(7 - sleep_hours) * 12
    
    if sleep_quality == "Poor":
        score -= 15
    elif sleep_quality == "Very Poor":
        score -= 25
    
    return max(min(score, 100), 0)


def emotional_drift(mood, withdrawal, continued):
    score = 0
    
    if mood == "Anxious":
        score += 20
    elif mood == "Sad":
        score += 15
    
    if withdrawal:
        score += 25
        
    if continued:
        score += 20
        
    return min(score, 100)


def social_energy(isolation_score, face_hours):
    score = 100 - (isolation_score * 8) + (face_hours * 5)
    return max(min(score, 100), 0)


def life_discipline(exercise_hours):
    score = exercise_hours * 12
    return min(score, 100)


def balance_index(scores):
    return sum(scores) / len(scores)
