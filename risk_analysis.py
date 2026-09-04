import random

def calculate_risk_scores(project_data):
    if not project_data:
        return {
            "overall_success_probability": 0,
            "financial_risk": 0,
            "market_risk": 0,
            "technical_risk": 0,
            "operational_risk": 0,
            "risk_level": "Unknown"
        }
        
    industry = project_data.get('industry', 'Technology')
    budget = float(project_data.get('budget', 0))
    
    # Base heuristics
    financial_risk = 80 if budget < 50000 else 40 if budget > 500000 else 60
    market_risk = 70 if industry == 'Finance' else 50
    technical_risk = 85 if industry == 'Technology' else 45
    operational_risk = 60
    
    # Add some dynamic variance
    financial_risk = max(10, min(95, financial_risk + random.randint(-10, 10)))
    market_risk = max(10, min(95, market_risk + random.randint(-10, 10)))
    technical_risk = max(10, min(95, technical_risk + random.randint(-10, 10)))
    operational_risk = max(10, min(95, operational_risk + random.randint(-10, 10)))
    
    avg_risk = (financial_risk + market_risk + technical_risk + operational_risk) / 4
    success_probability = int(100 - avg_risk)
    
    risk_level = "High" if success_probability < 40 else "Medium" if success_probability < 70 else "Low"
    
    return {
        "overall_success_probability": success_probability,
        "financial_risk": financial_risk,
        "market_risk": market_risk,
        "technical_risk": technical_risk,
        "operational_risk": operational_risk,
        "risk_level": risk_level
    }

def generate_swot(project_data):
    if not project_data:
        return {"Strengths": [], "Weaknesses": [], "Opportunities": [], "Threats": []}
        
    industry = project_data.get('industry', 'Technology')
    model = project_data.get('business_model', 'SaaS')
    
    swot = {
        "Strengths": [
            f"Scalable {model} architecture",
            "High margin potential",
            "Innovative approach to traditional problems"
        ],
        "Weaknesses": [
            "High initial customer acquisition cost",
            "Requires specialized talent",
            "Limited brand recognition initially"
        ],
        "Opportunities": [
            f"Growing demand in {industry} sector",
            "Potential for strategic partnerships",
            "Underserved niche markets"
        ],
        "Threats": [
            "Intense competition from established players",
            "Rapid technological changes",
            "Economic downturn affecting client budgets"
        ]
    }
    
    # Customize slightly based on industry
    if industry == "Healthcare":
        swot["Threats"].append("Strict regulatory compliance (HIPAA, etc.)")
        swot["Strengths"].append("Addresses critical, inelastic demand")
    elif industry == "Finance":
        swot["Threats"].append("Complex financial regulations")
        swot["Opportunities"].append("Integration with emerging decentralized systems")
        
    return swot
