def calculate_risk(
    market_competition,
    team_expertise,
    resource_availability,
    innovation_level,
    market_research,
):
    
    #this function calculates the overall project risk score
    risk = 0
    #market competition
    if market_competition == "High":
        risk += 25
    elif market_competition == "Medium":
        risk += 15
    else:
        risk += 5

    #team expertise
    if team_expertise == "Low":
        risk += 20
    elif team_expertise == "Medium":
        risk += 10
    else:
        risk += 5

    # resource availability
    if resource_availability == "Limited":
        risk += 20
    elif resource_availability == "Moderate":
        risk += 10
    else:
        risk += 5

    #innovation level
    if innovation_level == "Low":
        risk += 20
    elif innovation_level == "Medium":
        risk += 10
    else:
        risk += 5

    # market research
    if market_research == "Limited":
        risk += 15
    elif market_research == "Moderate":
        risk += 8
    else:
        risk += 3

    # keeping the score within the defined 0-100 range
    return min(risk, 100)


def get_risk_status(score):
    if score >= 70:
        return "HIGH RISK"
    elif score >= 40:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def calculate_success_probability(risk_score):
    #this converts the risk score into the project's success probability

    #Success Probability = 100 - Risk Score
    return max(0, 100 - risk_score)
