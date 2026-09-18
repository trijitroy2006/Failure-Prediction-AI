def generate_recommendations(
    project_data,
    risk_data,
    swot_data,
    feasibility_score
):
    # Generate recommendations based on the provided risk assessment and project parameters.

    recommendations = []

    #extract risk information

    market_competition = risk_data.get(
        "market_competition", ""
    )

    team_expertise = risk_data.get(
        "team_expertise", ""
    )

    resource_availability = risk_data.get(
        "resource_availability", ""
    )

    innovation_level = risk_data.get(
        "innovation_level", ""
    )

    market_research = risk_data.get(
        "market_research", ""
    )

    risk_score = risk_data.get(
        "risk_score", 0
    )

    #market recommendations 
    if market_competition == "High":

        recommendations.append({
            "category": "Market",
            "title": "Build Differentiation Strategy",
            "priority": "High",
            "problem": "High market competition",
            "explanation": (
                "The project is operating in a highly competitive "
                "market, which can make customer acquisition difficult."
            ),
            "action": (
                "Develop unique features, stronger positioning, "
                "and a clear competitive advantage."
            ),
            "risk_reduction": (
                "Differentiation can help the project stand out "
                "from established competitors."
            )
        })

    elif market_competition == "Medium":

        recommendations.append({
            "category": "Market",
            "title": "Strengthen Market Positioning",
            "priority": "Medium",
            "problem": "Moderate market competition",
            "explanation": (
                "The project faces competition and needs a clear "
                "position in the target market."
            ),
            "action": (
                "Define the unique value proposition and target "
                "customer segment more clearly."
            ),
            "risk_reduction": (
                "Clear positioning can improve customer targeting "
                "and competitive differentiation."
            )
        })

    elif market_competition == "Low":

        recommendations.append({
            "category": "Market",
            "title": "Explore Market Expansion",
            "priority": "Medium",
            "problem": "Low market competition",
            "explanation": (
                "Lower competition may provide an opportunity "
                "to explore additional market segments."
            ),
            "action": (
                "Investigate new customer segments and potential "
                "market expansion opportunities."
            ),
            "risk_reduction": (
                "Diversifying the target market can create "
                "additional growth opportunities."
            )
        })

    #technical recommendations

    if team_expertise == "Low":

        recommendations.append({
            "category": "Technical",
            "title": "Strengthen Technical Team",
            "priority": "Critical",
            "problem": "Limited technical expertise",
            "explanation": (
                "Limited expertise can increase development "
                "and implementation risks."
            ),
            "action": (
                "Hire specialists, provide targeted training, "
                "or work with external technical experts."
            ),
            "risk_reduction": (
                "Additional expertise can reduce technical "
                "errors and development delays."
            )
        })

    elif team_expertise == "Medium":

        recommendations.append({
            "category": "Technical",
            "title": "Improve Team Capabilities",
            "priority": "Medium",
            "problem": "Moderate technical expertise",
            "explanation": (
                "The team has basic capabilities but may need "
                "additional expertise for complex requirements."
            ),
            "action": (
                "Provide targeted training and add specialists "
                "where important skill gaps exist."
            ),
            "risk_reduction": (
                "Improved capabilities can reduce dependency "
                "on limited technical knowledge."
            )
        })

    if innovation_level == "Low":

        recommendations.append({
            "category": "Technical",
            "title": "Increase Product Innovation",
            "priority": "High",
            "problem": "Low innovation level",
            "explanation": (
                "Limited innovation may make it difficult to "
                "differentiate the project."
            ),
            "action": (
                "Explore new technologies, product features, "
                "or innovative approaches."
            ),
            "risk_reduction": (
                "Greater innovation can improve differentiation "
                "and competitive advantage."
            )
        })

    #financial recommendations

    if resource_availability == "Limited":

        recommendations.append({
            "category": "Financial",
            "title": "Secure Additional Funding",
            "priority": "Critical",
            "problem": "Limited available resources",
            "explanation": (
                "Limited resources may restrict development, "
                "marketing, and operational activities."
            ),
            "action": (
                "Explore funding options such as investment, "
                "grants, partnerships, or additional capital."
            ),
            "risk_reduction": (
                "Additional funding can increase financial "
                "runway and support essential activities."
            )
        })

        recommendations.append({
            "category": "Financial",
            "title": "Optimize Operational Costs",
            "priority": "High",
            "problem": "Resource constraints",
            "explanation": (
                "Limited resources require careful allocation "
                "of available funds."
            ),
            "action": (
                "Prioritize essential activities and reduce "
                "unnecessary operational expenses."
            ),
            "risk_reduction": (
                "Better cost management can extend the "
                "project's available financial runway."
            )
        })

    elif resource_availability == "Moderate":

        recommendations.append({
            "category": "Financial",
            "title": "Improve Resource Allocation",
            "priority": "Medium",
            "problem": "Moderate resource availability",
            "explanation": (
                "Available resources should be focused on "
                "the activities with the highest impact."
            ),
            "action": (
                "Prioritize spending toward core product "
                "development and market validation."
            ),
            "risk_reduction": (
                "Better allocation can reduce unnecessary "
                "financial pressure."
            )
        })

    #operational recommendations

    if market_research == "Limited":

        recommendations.append({
            "category": "Operational",
            "title": "Conduct Deeper Market Research",
            "priority": "High",
            "problem": "Limited market research",
            "explanation": (
                "Insufficient market information can lead to "
                "incorrect assumptions about customers and demand."
            ),
            "action": (
                "Conduct customer interviews, surveys, competitor "
                "research, and market validation."
            ),
            "risk_reduction": (
                "Better market information can reduce uncertainty "
                "before major project decisions."
            )
        })

    elif market_research == "Moderate":

        recommendations.append({
            "category": "Operational",
            "title": "Validate Market Assumptions",
            "priority": "Medium",
            "problem": "Moderate market research",
            "explanation": (
                "Some market information is available, but "
                "important assumptions may still need validation."
            ),
            "action": (
                "Collect additional customer feedback and "
                "validate key market assumptions."
            ),
            "risk_reduction": (
                "Validation can reduce uncertainty around "
                "customer demand."
            )
        })

    #overall risk recommendations

    if risk_score >= 70:

        recommendations.append({
            "category": "Risk",
            "title": "Prioritize High-Risk Areas",
            "priority": "Critical",
            "problem": "High overall project risk",
            "explanation": (
                "The current risk score indicates that several "
                "project factors require immediate attention."
            ),
            "action": (
                "Address the highest-impact risks before "
                "committing significant additional resources."
            ),
            "risk_reduction": (
                "Resolving major risks can improve project "
                "stability and feasibility."
            )
        })

    elif risk_score >= 40:

        recommendations.append({
            "category": "Risk",
            "title": "Monitor Key Project Risks",
            "priority": "High",
            "problem": "Moderate overall project risk",
            "explanation": (
                "The project has identifiable risks that "
                "should be actively monitored."
            ),
            "action": (
                "Create mitigation plans and regularly review "
                "the major risk factors."
            ),
            "risk_reduction": (
                "Continuous monitoring can prevent moderate "
                "risks from becoming critical."
            )
        })

    #feasibility recommendations

    if feasibility_score < 40:

        recommendations.append({
            "category": "Strategy",
            "title": "Validate the Project Before Scaling",
            "priority": "Critical",
            "problem": "Low project feasibility",
            "explanation": (
                "The current feasibility assessment indicates "
                "that important project assumptions need attention."
            ),
            "action": (
                "Validate the product, market demand, team "
                "capability, and resource requirements before scaling."
            ),
            "risk_reduction": (
                "Early validation can reduce the risk of "
                "committing significant resources to an unvalidated idea."
            )
        })

    elif feasibility_score < 60:

        recommendations.append({
            "category": "Strategy",
            "title": "Strengthen Project Feasibility",
            "priority": "High",
            "problem": "Moderate project feasibility",
            "explanation": (
                "The project appears potentially feasible, "
                "but some areas require improvement."
            ),
            "action": (
                "Improve market opportunity, team capability, "
                "competitive advantage, or resource planning."
            ),
            "risk_reduction": (
                "Improving weak feasibility factors can "
                "increase the project's overall viability."
            )
        })

    #priority order

    priority_order = {
        "Critical": 1,
        "High": 2,
        "Medium": 3
    }

    recommendations.sort(
        key=lambda item: priority_order.get(
            item["priority"],
            4
        )
    )

    #short term action plan

    short_term_actions = []

    for recommendation in recommendations:
        if recommendation["priority"] in ["Critical", "High"]:
            short_term_actions.append(
                recommendation["action"]
            )

    #keep the plan concise
    short_term_actions = short_term_actions[:5]

    #long term action plan 

    long_term_actions = [
        "Continuously monitor project risks and market conditions.",
        "Strengthen the team's technical and operational capabilities.",
        "Expand the product based on validated customer requirements.",
        "Review competitive positioning as the market changes."
    ]

    #final result 

    return {
        "overall_strategic_recommendation": (
            "Focus on reducing the highest-priority risks "
            "while improving market positioning, technical "
            "capability, and project feasibility."
        ),

        "recommendations": recommendations,

        "short_term_action_plan": short_term_actions,

        "long_term_action_plan": long_term_actions
    }