def calculate_feasibility(
    market_opportunity,
    team_capability,
    competitive_advantage,
    resource_availability,
):
    # Calculate the average feasibility score
    score = (
        market_opportunity
        + team_capability
        + competitive_advantage
        + resource_availability
    ) / 4

    return round(score)