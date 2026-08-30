def get_market_data(industry="Technology", target_market=""):
    industry_data = {
        "Technology": {"TAM": "$2.4B", "SAM": "$850M", "SOM": "$12M", "growth": ["+8.2%", "+5.3%", "-2.3%"]},
        "Healthcare": {"TAM": "$3.1B", "SAM": "$1.2B", "SOM": "$45M", "growth": ["+9.1%", "+6.2%", "+1.5%"]},
        "Finance": {"TAM": "$4.5B", "SAM": "$1.8B", "SOM": "$80M", "growth": ["+7.4%", "+4.8%", "+2.1%"]},
        "Education": {"TAM": "$1.2B", "SAM": "$400M", "SOM": "$8M", "growth": ["+5.5%", "+3.2%", "-1.1%"]}
    }
    
    data = industry_data.get(industry, industry_data["Technology"])
    
    return {
        "TAM": {"value": data["TAM"], "growth": data["growth"][0], "trend": "up" if "+" in data["growth"][0] else "down"},
        "SAM": {"value": data["SAM"], "growth": data["growth"][1], "trend": "up" if "+" in data["growth"][1] else "down"},
        "SOM": {"value": data["SOM"], "growth": data["growth"][2], "trend": "up" if "+" in data["growth"][2] else "down"}
    }

def get_competitor_data(startup_name="", industry="Technology"):
    if industry == "Healthcare":
        names = ["HealthCorp", "MediTech Solutions", "CarePlus AI"]
    elif industry == "Finance":
        names = ["FinServe", "WealthTech Inc.", "PayStream"]
    elif industry == "Education":
        names = ["EduSmart", "LearnHub", "SkillForge"]
    else:
        names = ["TechGiant A", "InnovateTech", "NextGen Solutions"]
        
    return [
        {"name": names[0], "type": "DIRECT", "market_share": "28%", "revenue": "$45M", "growth": "+12%", "position": 80},
        {"name": names[1], "type": "DIRECT", "market_share": "22%", "revenue": "$38M", "growth": "+8%", "position": 60},
        {"name": names[2], "type": "INDIRECT", "market_share": "15%", "revenue": "$25M", "growth": "+5%", "position": 40}
    ]
