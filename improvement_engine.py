"""Generate project improvements from market analysis and risk mitigations."""

import re


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


def _growth_rate(market_data, segment):
    """Read a signed percentage from a market-analysis segment."""
    growth = str(market_data.get(segment, {}).get("growth", "0%"))
    match = re.search(r"[-+]?\d+(?:\.\d+)?", growth)
    return float(match.group()) if match else 0.0


def generate_improvements(
    project_data,
    risk_data,
    swot_data,
    feasibility_score,
    market_data=None,
    mitigation_results=None,
):
    """Return improvements grounded in market metrics and generated mitigations.

    ``market_data`` must be the result of ``market_analysis.get_market_data`` and
    ``mitigation_results`` must be the result of ``generate_mitigation``. The
    original arguments remain supported so callers can migrate incrementally.
    """
    project_data = project_data or {}
    risk_data = risk_data or {}
    swot_data = swot_data or {}
    market_data = market_data or {}
    mitigation_results = mitigation_results or []
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

    tam_growth = _growth_rate(market_data, "TAM")
    sam_growth = _growth_rate(market_data, "SAM")
    som_growth = _growth_rate(market_data, "SOM")

    if market_data and min(tam_growth, sam_growth, som_growth) < 0:
        recommendations.append(_recommendation(
            "Market",
            "Respond to Market Contraction",
            "High",
            f"The market analysis shows a declining growth signal in {industry}, which may reduce demand for {target_market}.",
            [
                "Identify which market segment produced the negative growth signal and interview current and lost customers.",
                "Adjust the product positioning, pricing, or target segment around the strongest validated demand.",
                "Run a small pilot and track qualified leads, conversion, and retention before increasing spend.",
            ],
            "The project can move toward healthier demand instead of scaling against a declining market signal.",
        ))
    elif market_data and som_growth < sam_growth:
        recommendations.append(_recommendation(
            "Market",
            "Convert Addressable Demand into Adoption",
            "High" if market_competition == "High" else "Medium",
            f"The obtainable market is growing more slowly than the serviceable market, indicating an adoption or positioning gap for {target_market}.",
            [
                "Compare the target customer's buying barriers with the current product and pricing proposition.",
                "Test one focused acquisition channel with a measurable conversion target.",
                "Use pilot feedback to improve onboarding and repeat the test before expanding channels.",
            ],
            "Improving conversion from the available market increases realistic adoption rather than relying only on total market size.",
        ))
    elif market_competition in {"High", "Medium"}:
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

    mitigation_improvements = {
        "financial": (
            "Protect the Delivery Runway",
            "Available resources may be consumed before the project proves demand.",
            "Separate essential milestone costs from optional spending; track the budget weekly; delay non-essential commitments until validation.",
            "The mitigation plan is strengthened by tying every expense to a measurable delivery or validation milestone.",
        ),
        "market": (
            "Turn Market Monitoring into Validation",
            "The market risk mitigation requires ongoing monitoring, but decisions may still be based on untested assumptions.",
            "Interview target customers; compare competitor positioning monthly; test pricing or positioning changes with a pilot.",
            "Regular evidence turns market monitoring into faster positioning decisions and lowers demand uncertainty.",
        ),
        "technical": (
            "Close the Technical Delivery Gap",
            "Technical risk mitigation depends on testing and expertise that may not yet be consistently available.",
            "List the skills needed for the next milestone; assign training or specialist support; add testing and code review gates.",
            "A repeatable delivery process reduces defects, rework, and milestone delays.",
        ),
        "operational": (
            "Standardize Operational Controls",
            "Operational risk can recur when responsibilities and fallback processes are not explicit.",
            "Document the critical workflow; assign an owner; test the backup process before the next milestone.",
            "Clear ownership and tested fallbacks make project execution more reliable.",
        ),
    }

    for mitigation in mitigation_results:
        category_key = str(mitigation.get("category", "general")).lower()
        template = mitigation_improvements.get(category_key)
        if not template:
            continue
        title, problem, action, benefit = template
        risk = mitigation.get("risk", "the identified project risk")
        recommendations.append(_recommendation(
            mitigation.get("category", "Risk"),
            title,
            mitigation.get("priority", "Medium"),
            f"{problem} Identified risk: {risk}.",
            [part.strip() for part in action.split(";")],
            benefit,
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

    if resource_availability in {"Limited", "Moderate"} and not any(
        item["category"] == "Financial" for item in recommendations
    ):
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

    if market_research in {"Limited", "Moderate"} and not any(
        item["category"] == "Market" for item in recommendations
    ):
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