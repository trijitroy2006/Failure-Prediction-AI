# Milestone 3 - Risk Mitigation Engine


def generate_mitigation(risk_data):
    """
    Generate mitigation strategies from Milestone 2 risk data.

    Parameters:
        risk_data: list of risk dictionaries

    Returns:
        list of mitigation dictionaries
    """

    mitigation_results = []

    if not risk_data:
        return mitigation_results

    for risk in risk_data:

        category = risk.get(
            "risk_category",
            risk.get("category", "General")
        )

        description = risk.get(
            "risk_description",
            risk.get("description", "Risk identified in the project")
        )

        score = risk.get(
            "risk_score",
            risk.get("score", 0)
        )

        priority = risk.get(
            "priority_level",
            risk.get("priority", "Medium")
        )

        # Convert score safely
        try:
            score = float(score)
        except (ValueError, TypeError):
            score = 0

        # Determine impact
        if score >= 75:
            impact = "High"
        elif score >= 50:
            impact = "Medium"
        else:
            impact = "Low"

        # Category-specific mitigation
        category_lower = str(category).lower()

        if category_lower == "financial":

            mitigation = (
                "Monitor project expenses and maintain a "
                "contingency budget to control financial risk."
            )

            preventive = (
                "Perform regular budget reviews and track "
                "project expenditure against planned costs."
            )

            contingency = (
                "Reduce non-critical expenses and reallocate "
                "the available budget if costs increase."
            )

        elif category_lower == "market":

            mitigation = (
                "Continuously monitor competitors, customer "
                "demand and market trends."
            )

            preventive = (
                "Perform regular market research and validate "
                "customer requirements."
            )

            contingency = (
                "Adjust pricing, positioning or target market "
                "if market conditions change."
            )

        elif category_lower == "technical":

            mitigation = (
                "Reduce technical risk through testing, code "
                "reviews and appropriate technical expertise."
            )

            preventive = (
                "Perform regular testing, code reviews and "
                "technical feasibility checks."
            )

            contingency = (
                "Use an alternative technology or allocate "
                "additional technical resources when required."
            )

        elif category_lower == "operational":

            mitigation = (
                "Improve operational reliability using "
                "documented processes and continuous monitoring."
            )

            preventive = (
                "Define responsibilities and document important "
                "operational workflows."
            )

            contingency = (
                "Activate backup processes and reassign resources "
                "when operational problems occur."
            )

        elif category_lower == "regulatory":

            mitigation = (
                "Monitor regulatory requirements and perform "
                "regular compliance reviews."
            )

            preventive = (
                "Review applicable regulations before major "
                "project releases."
            )

            contingency = (
                "Modify the affected process or implementation "
                "to satisfy updated requirements."
            )

        else:

            mitigation = (
                "Monitor the identified risk continuously and "
                "introduce appropriate controls."
            )

            preventive = (
                "Track risk indicators and perform regular "
                "risk reviews."
            )

            contingency = (
                "Activate a fallback plan and allocate "
                "additional resources when necessary."
            )

        mitigation_results.append({
            "risk": description,
            "category": category,
            "risk_score": score,
            "impact": impact,
            "priority": priority,
            "mitigation_strategy": mitigation,
            "preventive_action": preventive,
            "contingency_action": contingency
        })

    return mitigation_results


# Simple test
if __name__ == "__main__":

    sample_risks = [
        {
            "risk_category": "Technical",
            "risk_score": 80,
            "risk_description": "Limited technical expertise",
            "priority_level": "High"
        },
        {
            "risk_category": "Market",
            "risk_score": 65,
            "risk_description": "High competitor density",
            "priority_level": "Medium"
        }
    ]

    results = generate_mitigation(sample_risks)

    for result in results:
        print("\nRisk:", result["risk"])
        print("Category:", result["category"])
        print("Impact:", result["impact"])
        print("Priority:", result["priority"])
        print("Mitigation:", result["mitigation_strategy"])
        print("Preventive:", result["preventive_action"])
        print("Contingency:", result["contingency_action"])