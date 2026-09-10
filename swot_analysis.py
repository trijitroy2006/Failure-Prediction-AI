def generate_swot(team_expertise, innovation_level, market_competition, resource_availability, market_research):
    strengths = ["Unique AI algorithm" if innovation_level == "High" else "Clear value proposition"]
    if team_expertise == "High":
        strengths.append("Strong technical team")
    else:
        strengths.append("Lean and agile operations")
    strengths.append("Early mover advantage")
    if resource_availability == "Good":
        strengths.append("Scalable architecture")

    weaknesses = []
    if market_research == "Limited":
        weaknesses.append("Limited market research")
    else:
        weaknesses.append("Niche market focus")
    if resource_availability == "Limited":
        weaknesses.append("Small marketing budget")
    weaknesses.append("No brand recognition")
    if team_expertise == "Low":
        weaknesses.append("Dependency on key personnel")

    opportunities = ["Growing market demand"]
    if market_competition == "Low":
        opportunities.append("Blue ocean strategy")
    opportunities.append("Partnership potential")
    opportunities.append("Expansion to new verticals")
    opportunities.append("International markets")

    threats = []
    if market_competition == "High":
        threats.append("Established competitors")
    threats.append("Rapid tech changes")
    threats.append("Regulatory uncertainty")
    threats.append("Economic downturn")

    return {
        "Strengths": strengths,
        "Weaknesses": weaknesses,
        "Opportunities": opportunities,
        "Threats": threats
    }
