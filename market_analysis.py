def get_market_data(industry="Technology", target_market="", budget=0):
    industry_data = {
        "Technology": {"TAM_base": 2.4, "SAM_base": 850, "SOM_base": 12, "growth": ["+8.2%", "+5.3%", "-2.3%"]},
        "Healthcare": {"TAM_base": 3.1, "SAM_base": 1200, "SOM_base": 45, "growth": ["+9.1%", "+6.2%", "+1.5%"]},
        "Finance": {"TAM_base": 4.5, "SAM_base": 1800, "SOM_base": 80, "growth": ["+7.4%", "+4.8%", "+2.1%"]},
        "Education": {"TAM_base": 1.2, "SAM_base": 400, "SOM_base": 8, "growth": ["+5.5%", "+3.2%", "-1.1%"]}
    }
    
    data = industry_data.get(industry, industry_data["Technology"])
    
    # Dynamic scaling based on budget
    multiplier = 1.0 + (budget / 1000000.0) if budget else 1.0
    
    tam_val = f"${data['TAM_base']:.1f}B"
    sam_val = f"${int(data['SAM_base'] * multiplier)}M"
    som_val = f"${int(data['SOM_base'] * multiplier)}M"
    
    return {
        "TAM": {"value": tam_val, "growth": data["growth"][0], "trend": "up" if "+" in data["growth"][0] else "down"},
        "SAM": {"value": sam_val, "growth": data["growth"][1], "trend": "up" if "+" in data["growth"][1] else "down"},
        "SOM": {"value": som_val, "growth": data["growth"][2], "trend": "up" if "+" in data["growth"][2] else "down"}
    }

def get_competitor_data(startup_name="", industry="Technology", business_model="SaaS"):
    if industry == "Healthcare":
        names = ["HealthCorp", "MediTech Solutions", f"CarePlus {business_model}"]
    elif industry == "Finance":
        names = ["FinServe", "WealthTech Inc.", f"{business_model} Stream"]
    elif industry == "Education":
        names = ["EduSmart", "LearnHub", f"SkillForge {business_model}"]
    else:
        names = ["TechGiant A", "InnovateTech", f"NextGen {business_model}"]
        
    return [
        {"name": names[0], "type": "DIRECT", "market_share": "28%", "revenue": "$45M", "growth": "+12%", "position": 80},
        {"name": names[1], "type": "DIRECT", "market_share": "22%", "revenue": "$38M", "growth": "+8%", "position": 60},
        {"name": names[2], "type": "INDIRECT", "market_share": "15%", "revenue": "$25M", "growth": "+5%", "position": 40}
    ]
