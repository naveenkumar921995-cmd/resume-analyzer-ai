def calculate_ats(match_score, skill_count):
    ats = (match_score * 0.6) + (skill_count * 2)
    return min(round(ats, 2), 100)
