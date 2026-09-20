import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def build_prompt(project_data, risk_data, swot_data, feasibility_score):
    prompt = f"""
You are a startup risk advisor. Based on the following project data, generate 3 to 5 actionable recommendations.

Project Name: {project_data.get('startup_name', 'Unknown')}
Industry: {project_data.get('industry', 'Unknown')}

Risk Factors:
- Market Competition: {risk_data.get('market_competition', 'Unknown')}
- Team Expertise: {risk_data.get('team_expertise', 'Unknown')}
- Resource Availability: {risk_data.get('resource_availability', 'Unknown')}
- Innovation Level: {risk_data.get('innovation_level', 'Unknown')}
- Market Research: {risk_data.get('market_research', 'Unknown')}
- Overall Risk Score: {risk_data.get('risk_score', 'Unknown')}

Feasibility Score: {feasibility_score}

SWOT Summary:
Strengths: {swot_data.get('strengths', [])}
Weaknesses: {swot_data.get('weaknesses', [])}
Opportunities: {swot_data.get('opportunities', [])}
Threats: {swot_data.get('threats', [])}

Return ONLY valid JSON, no extra text, no markdown formatting, in this exact format:
[
  {{
    "category": "Market",
    "title": "short title",
    "priority": "Critical" or "High" or "Medium",
    "problem": "one line problem statement",
    "action": "1-2 sentence concrete action",
    "risk_reduction": "1 sentence on how this action reduces risk"
  }}
]
"""
    return prompt


def generate_llm_recommendations(project_data, risk_data, swot_data, feasibility_score):
    prompt = build_prompt(project_data, risk_data, swot_data, feasibility_score)
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        text = response.text.strip()

        if text.startswith("```"):
            text = text.strip("`")
            if text.startswith("json"):
                text = text[4:]

        recommendations = json.loads(text)
        return recommendations

    except Exception as e:
        print("LLM recommendation generation failed:", e)
        return None