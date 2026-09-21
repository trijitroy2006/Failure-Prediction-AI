"""Generate targeted project improvement suggestions for the Recommendations tab."""


def _recommendation(category, title, priority, problem, steps, benefit):
    """Keep the recommendation shape compatible with the existing Tab 3 cards."""
    return {
        "category": category,
        "title": title,
        "priority": priority,
        "problem": problem,
        "steps": steps,
        "action": " ".join(
            f"{index}. {step}" for index, step in enumerate(steps, start=1)
        ),
        "improvement": benefit,
        "risk_reduction": benefit,
    }


def generate_improvements(project_data, risk_data, swot_data, feasibility_score):
    """Return improvements targeted to the project's weakest assessed areas.

    The function is deterministic so recommendations remain available without an
    external model or API key. Inputs match the values already calculated for Tab 2.
    """
    project_data = project_data or {}
    risk_data = risk_data or {}
    swot_data = swot_data or {}
    recommendations = []

    market_competition = risk_data.get("market_competition", "Medium")
    team_expertise = risk_data.get("team_expertise", "Medium")
    resource_availability = risk_data.get("resource_availability", "Moderate")
    innovation_level = risk_data.get("innovation_level", "Medium")
    market_research = risk_data.get("market_research", "Moderate")
    risk_score = risk_data.get("risk_score", 0)
    industry = project_data.get("industry", "the target industry")
    target_market = project_data.get("target_market", "the target customer segment")
    feasibility_score = int(feasibility_score or 0)

    if market_competition in {"High", "Medium"}:
        recommendations.append(_recommendation(
            "Market",
            "Sharpen the Competitive Position",
            "High" if market_competition == "High" else "Medium",
            f"{industry} competition may make it difficult to win and retain {target_market} customers.",
            [
                "Interview at least five target customers about their current alternatives and unmet needs.",
                "Select one high-value problem the project will solve better than competitors.",
                "Turn that choice into a measurable value proposition and test it with a landing page or pilot.",
            ],
            "A validated, focused position improves customer acquisition efficiency and gives product work a clear priority.",
        ))

    if team_expertise in {"Low", "Medium"}:
        recommendations.append(_recommendation(
            "Team",
            "Close the Capability Gaps",
            "Critical" if team_expertise == "Low" else "High",
            "The current team capability may not cover all skills needed to deliver and operate the project reliably.",
            [
                "List the technical and business skills required for the next delivery milestone.",
                "Assign each gap to a training plan, a specialist hire, or a trusted external partner.",
                "Review delivery quality and milestone completion at the end of each sprint.",
            ],
            "The project gains dependable execution capacity, reducing delays, rework, and reliance on a single team member.",
        ))

    if resource_availability in {"Limited", "Moderate"}:
        recommendations.append(_recommendation(
            "Financial",
            "Protect the Delivery Runway",
            "Critical" if resource_availability == "Limited" else "High",
            "Available resources may be consumed before the project proves demand or reaches its next milestone.",
            [
                "Separate essential milestone costs from optional spending and rank them by expected project impact.",
                "Set a monthly budget limit and track actual spend against it every week.",
                "Delay non-essential commitments until the next validation milestone is achieved.",
            ],
            "Focused spending extends the runway and keeps enough resources available for the work that proves viability.",
        ))

    if innovation_level in {"Low", "Medium"}:
        recommendations.append(_recommendation(
            "Product",
            "Increase Differentiated Product Value",
            "High" if innovation_level == "Low" else "Medium",
            "The product may be difficult to distinguish if its benefits are similar to existing alternatives.",
            [
                "Map the top competitor features against the customer problems they leave unresolved.",
                "Prototype one differentiated capability that directly addresses the most important gap.",
                "Measure adoption, task completion, or customer willingness to pay during a pilot.",
            ],
            "Evidence-backed differentiation improves competitive advantage without spending heavily on untested features.",
        ))

    if market_research in {"Limited", "Moderate"}:
        recommendations.append(_recommendation(
            "Validation",
            "Validate the Highest-Risk Assumptions",
            "High" if market_research == "Limited" else "Medium",
            "Incomplete market evidence can lead the project to build for customers who do not have a strong enough need.",
            [
                "Write down assumptions about the customer, problem, buying process, and expected price.",
                "Test the riskiest assumption with interviews, a prototype, or a small paid pilot.",
                "Record the evidence and update the product scope when the results contradict an assumption.",
            ],
            "Fast validation prevents wasted development and makes investment decisions more evidence-based.",
        ))

    if risk_score >= 70 or feasibility_score < 60:
        recommendations.append(_recommendation(
            "Strategy",
            "Use Milestone-Based Risk Reviews",
            "Critical" if risk_score >= 70 else "High",
            "The combined risk and feasibility results show that scaling before resolving weak areas could increase losses.",
            [
                "Choose three measurable gates for demand, delivery capability, and financial runway.",
                "Review the gates before each major release or funding decision.",
                "Continue, revise, or pause the project based on the evidence at each gate.",
            ],
            "Milestone gates limit irreversible commitments and keep improvement work aligned with project viability.",
        ))

    weaknesses = swot_data.get("Weaknesses", []) if isinstance(swot_data, dict) else []
    if not recommendations and weaknesses:
        recommendations.append(_recommendation(
            "Strategy",
            "Resolve the Leading SWOT Weakness",
            "Medium",
            f"The SWOT assessment identifies a weakness: {weaknesses[0]}.",
            [
                "Translate the weakness into one measurable project outcome.",
                "Assign an owner and a deadline for the first corrective action.",
                "Review the outcome at the next project milestone and adjust the plan.",
            ],
            "An owned, measurable corrective action turns the SWOT finding into visible project progress.",
        ))

    priority_order = {"Critical": 1, "High": 2, "Medium": 3}
    recommendations.sort(key=lambda item: priority_order.get(item["priority"], 4))
    return recommendations