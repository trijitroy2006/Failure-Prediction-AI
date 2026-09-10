import streamlit as st
import pandas as pd
import market_analysis


st.set_page_config(page_title="Failure Prediction AI", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to mimic the Mac-style window from the PDF
st.markdown("""
<style>
    /* Main container styling to look like a window */
    .main .block-container {
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.1);
        padding: 2rem !important;
        margin-top: 3rem;
        margin-bottom: 3rem;
        border: 1px solid #BFDBFE;
    }

    /* Mac window controls (Red, Yellow, Green dots) */
    .mac-controls {
        display: flex;
        gap: 8px;
        margin-bottom: 20px;
        margin-top: -10px;
    }
    .mac-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    .mac-red { background-color: #ff5f56; }
    .mac-yellow { background-color: #ffbd2e; }
    .mac-green { background-color: #27c93f; }

    /* Customizing the tabs to look more like the PDF */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        border-bottom: 1px solid #e5e7eb;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
        color: #6b7280;
    }
    .stTabs [aria-selected="true"] {
        color: #111827;
        border-bottom: 2px solid #3b82f6;
    }
    
    /* Adjusting headers */
    h1 {
        font-size: 2.2rem !important;
        padding-bottom: 0 !important;
    }
    
</style>
""", unsafe_allow_html=True)

# Injecting the Mac dots at the top of the container
st.markdown("""
<div class="mac-controls">
    <div class="mac-dot mac-red"></div>
    <div class="mac-dot mac-yellow"></div>
    <div class="mac-dot mac-green"></div>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Project Input", "Risk Assessment", "Recommendations", "Dashboard"])

with tab1:
    st.markdown("""
    <div style="background-color: #FEE2E2; color: #DC2626; padding: 4px 12px; border-radius: 16px; display: inline-block; font-size: 0.75rem; font-weight: 700; margin-bottom: 8px; font-family: sans-serif;">
        ▲ MILESTONE 1 • WEEKS 1-2
    </div>
    <h1 style="margin: 0; padding: 0; font-size: 28px; color: #111827; font-weight: 700; font-family: sans-serif;">Data Collection & Market Intelligence</h1>
    <p style="margin: 4px 0 24px 0; color: #6B7280; font-size: 15px; font-family: sans-serif;">Gather project data and analyze market landscape</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Project Submission")
        with st.form("project_form"):
            startup_name = st.text_input("Startup/Project Name", "e.g., TechVenture AI")
            industry = st.selectbox("Industry/Sector", ["Technology", "Healthcare", "Finance", "Education"])
            business_model = st.selectbox("Business Model", ["SaaS", "B2B", "B2C", "Marketplace"])
            
            target_market = st.text_input("Target Market", "e.g., SMBs")
            budget = st.number_input("Budget (USD)", min_value=0, value=100000, step=10000)
                
            description = st.text_area("Project Description", "Brief description of your project idea...")
            
            submitted = st.form_submit_button("Analyze Project")
            
        if submitted:
            st.session_state['project_data'] = {
                "startup_name": startup_name,
                "industry": industry,
                "business_model": business_model,
                "target_market": target_market,
                "budget": budget,
                "description": description
            }

    with col2:
        st.subheader("Market Analysis")
        if 'project_data' in st.session_state:
            data = st.session_state['project_data']
            m_data = market_analysis.get_market_data(data['industry'], data['target_market'], data['budget'])
            
            st.write("**Market Size & Growth Rate**")
            
            m1, m2, m3 = st.columns(3)
            m1.metric("TAM", m_data['TAM']['value'], m_data['TAM']['growth'])
            m2.metric("SAM", m_data['SAM']['value'], m_data['SAM']['growth'])
            m3.metric("SOM", m_data['SOM']['value'], m_data['SOM']['growth'])
            
            st.write("**Market Trends (2020-2026)**")
            chart_data = pd.DataFrame(
                [30, 40, 45, 55, 70, 85, 100],
                columns=["Trend"],
                index=["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
            )
            st.bar_chart(chart_data)
            
        else:
            st.info("Submit a project idea on the left to view the market analysis.")

    with col3:
        st.subheader("Competitor Landscape")
        if 'project_data' in st.session_state:
            data = st.session_state['project_data']
            c_data = market_analysis.get_competitor_data(data['startup_name'], data['industry'], data['business_model'])
            
            for comp in c_data:
                with st.container():
                    st.markdown(f"**{comp['name']}** `{comp['type']}`")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Market Share", comp['market_share'])
                    c2.metric("Revenue", comp['revenue'])
                    c3.metric("Growth", comp['growth'])
                    st.progress(comp['position'] / 100, text="Market Position")
                    st.divider()
                    
        else:
            st.info("Submit a project idea to generate competitor insights.")

with tab2:
    st.markdown("""
    <div style="background-color: #FEE2E2; color: #DC2626; padding: 4px 12px; border-radius: 16px; display: inline-block; font-size: 0.75rem; font-weight: 700; margin-bottom: 8px; font-family: sans-serif;">
        📋 MILESTONE 2 • WEEKS 3-4
    </div>
    <h1 style="margin: 0; padding: 0; font-size: 28px; color: #111827; font-weight: 700; font-family: sans-serif;">Risk Assessment & SWOT Analysis</h1>
    <p style="margin: 4px 0 24px 0; color: #6B7280; font-size: 15px; font-family: sans-serif;">AI-powered risk scoring and strategic evaluation</p>
    """, unsafe_allow_html=True)

    if 'project_data' in st.session_state:
        data = st.session_state['project_data']
    else:
        data = {'industry': 'Technology', 'budget': 100000, 'startup_name': 'Demo Project'}
        
    # Algorithmically derive inputs from project_data
    market_competition = "High" if data.get('industry') == 'Technology' else "Medium"
    team_expertise = "Low" if data.get('budget', 0) < 50000 else "High"
    resource_availability = "Good" if data.get('budget', 0) >= 100000 else "Limited"
    innovation_level = "High"
    market_research = "Moderate"
    
    market_opportunity = 45 if market_competition == "High" else 75
    team_capability = 50 if team_expertise == "Low" else 85
    competitive_advantage = 35 if innovation_level == "Low" else 70
    resource_score = 65 if resource_availability == "Good" else 30

    from risk_engine import calculate_risk, get_risk_status, calculate_success_probability
    risk_score = calculate_risk(market_competition, team_expertise, resource_availability, innovation_level, market_research)
    risk_status = get_risk_status(risk_score)
    success_probability = calculate_success_probability(risk_score)

    from swot_analysis import generate_swot
    swot = generate_swot(team_expertise, innovation_level, market_competition, resource_availability, market_research)

    from feasibility import calculate_feasibility
    feasibility_score = calculate_feasibility(market_opportunity, team_capability, competitive_advantage, resource_score)

    # Format SWOT bullets as HTML dots
    def format_swot(items):
        return "".join([f'<div style="margin-bottom:4px;">• {item}</div>' for item in items])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # FINAL DASHBOARD LAYOUT (3 columns) matching PDF mockup perfectly
    r_col1, r_col2, r_col3 = st.columns([1, 1.5, 1])
    
    with r_col1:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 style="margin:0; font-size: 16px; color: #111827; font-family: sans-serif;">Risk Score</h3>
            <span style="color: #DC2626; font-size: 14px;">&#9888;</span>
        </div>
        <div style="border: 1px solid #E5E7EB; border-radius: 8px; padding: 24px; text-align: center; margin-bottom: 16px; background: white; font-family: sans-serif;">
            <div style="color: #6B7280; font-size: 12px; margin-bottom: 16px;">Overall Risk Score</div>
            <div style="color: #DC2626; font-size: 56px; font-weight: 800; line-height: 1;">{risk_score}</div>
            <div style="color: #DC2626; font-size: 11px; font-weight: 700; margin-top: 16px;">{risk_status}</div>
        </div>
        <div style="border: 1px solid #E5E7EB; border-radius: 8px; padding: 16px; margin-bottom: 24px; background: white; font-family: sans-serif;">
            <div style="color: #6B7280; font-size: 12px; margin-bottom: 12px;">Success Probability</div>
            <div style="background: #E5E7EB; border-radius: 4px; height: 6px; width: 100%; margin-bottom: 8px;">
                <div style="background: #DC2626; border-radius: 4px; height: 100%; width: {success_probability}%;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 600;">
                <span style="color: #111827;">{success_probability}%</span>
                <span style="color: #DC2626;">Low</span>
            </div>
        </div>
        <h4 style="font-size: 14px; margin-bottom: 12px; color: #111827; font-family: sans-serif;">Key Risk Factors</h4>
        <div style="border: 1px solid #E5E7EB; border-radius: 8px; padding: 12px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px; background: white; font-family: sans-serif;">
            <div style="background: #FEF3C7; color: #D97706; padding: 6px; border-radius: 6px; font-size: 16px; width: 32px; height: 32px; display: flex; justify-content: center; align-items: center;">&#128101;</div>
            <div>
                <div style="font-size: 13px; font-weight: 600; color: #111827;">Team Expertise</div>
                <div style="font-size: 11px; color: #6B7280;">{team_expertise} technical experience</div>
            </div>
        </div>
        <div style="border: 1px solid #E5E7EB; border-radius: 8px; padding: 12px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px; background: white; font-family: sans-serif;">
            <div style="background: #D1FAE5; color: #10B981; padding: 6px; border-radius: 6px; font-size: 16px; width: 32px; height: 32px; display: flex; justify-content: center; align-items: center;">&#128161;</div>
            <div>
                <div style="font-size: 13px; font-weight: 600; color: #111827;">Innovation Gap</div>
                <div style="font-size: 11px; color: #6B7280;">{innovation_level} innovation potential</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with r_col2:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-family: sans-serif;">
            <h3 style="margin:0; font-size: 16px; color: #111827;">SWOT Analysis</h3>
            <span style="color: #6B7280; font-size: 16px;">&#8862;</span>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-family: sans-serif;">
            <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; padding: 16px;">
                <div style="color: #16A34A; font-weight: 600; font-size: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
                    <span style="background: #16A34A; color: white; border-radius: 50%; width: 14px; height: 14px; display: inline-flex; align-items: center; justify-content: center; font-size: 10px;">+</span> Strengths
                </div>
                <div style="color: #111827; font-size: 12px; line-height: 1.5;">
                    {format_swot(swot["Strengths"])}
                </div>
            </div>
            <div style="background: #FEF2F2; border: 1px solid #FECACA; border-radius: 8px; padding: 16px;">
                <div style="color: #DC2626; font-weight: 600; font-size: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
                    <span style="background: #DC2626; color: white; border-radius: 50%; width: 14px; height: 14px; display: inline-flex; align-items: center; justify-content: center; font-size: 10px;">-</span> Weaknesses
                </div>
                <div style="color: #111827; font-size: 12px; line-height: 1.5;">
                    {format_swot(swot["Weaknesses"])}
                </div>
            </div>
            <div style="background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 8px; padding: 16px; min-height: 180px;">
                <div style="color: #2563EB; font-weight: 600; font-size: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
                    <span style="color: #2563EB; font-size: 16px;">&#8599;</span> Opportunities
                </div>
                <div style="color: #111827; font-size: 12px; line-height: 1.5;">
                    {format_swot(swot["Opportunities"])}
                </div>
            </div>
            <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 8px; padding: 16px; min-height: 180px;">
                <div style="color: #D97706; font-weight: 600; font-size: 14px; margin-bottom: 12px; display: flex; align-items: center; gap: 6px;">
                    <span style="color: #D97706; font-size: 14px;">&#9888;</span> Threats
                </div>
                <div style="color: #111827; font-size: 12px; line-height: 1.5;">
                    {format_swot(swot["Threats"])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with r_col3:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-family: sans-serif;">
            <h3 style="margin:0; font-size: 16px; color: #111827;">Project Feasibility</h3>
            <span style="color: white; background: #10B981; border-radius: 50%; width: 18px; height: 18px; display: inline-flex; align-items: center; justify-content: center; font-size: 10px;">&#10004;</span>
        </div>
        <div style="border: 1px solid #E5E7EB; border-radius: 8px; padding: 24px; text-align: center; margin-bottom: 24px; background: white; font-family: sans-serif;">
            <div style="color: #6B7280; font-size: 12px; margin-bottom: 16px;">Feasibility Score</div>
            <div style="color: #10B981; font-size: 48px; font-weight: 800; line-height: 1;">{feasibility_score}%</div>
            <div style="color: #9CA3AF; font-size: 10px; margin-top: 16px; line-height: 1.4; padding: 0 10px;">Moderate Feasibility with Significant Improvements Needed</div>
        </div>
        <h4 style="font-size: 14px; margin-bottom: 16px; color: #111827; font-family: sans-serif;">Assessment Metrics</h4>
        
        <div style="margin-bottom: 16px; font-family: sans-serif;">
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                <span style="color: #374151; font-weight: 500;">Team Capability</span>
                <span style="color: #F59E0B; font-weight: 600;">{team_capability}%</span>
            </div>
            <div style="background: #E5E7EB; border-radius: 4px; height: 4px; width: 100%;">
                <div style="background: #F59E0B; border-radius: 4px; height: 100%; width: {team_capability}%;"></div>
            </div>
        </div>
        <div style="margin-bottom: 16px; font-family: sans-serif;">
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                <span style="color: #374151; font-weight: 500;">Competitive Advantage</span>
                <span style="color: #DC2626; font-weight: 600;">{competitive_advantage}%</span>
            </div>
            <div style="background: #E5E7EB; border-radius: 4px; height: 4px; width: 100%;">
                <div style="background: #DC2626; border-radius: 4px; height: 100%; width: {competitive_advantage}%;"></div>
            </div>
        </div>
        <div style="margin-bottom: 16px; font-family: sans-serif;">
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
                <span style="color: #374151; font-weight: 500;">Resource Availability</span>
                <span style="color: #10B981; font-weight: 600;">{resource_score}%</span>
            </div>
            <div style="background: #E5E7EB; border-radius: 4px; height: 4px; width: 100%;">
                <div style="background: #10B981; border-radius: 4px; height: 100%; width: {resource_score}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)


with tab3:
    st.info("Recommendations coming soon")
with tab4:
    st.info("Dashboard coming soon")


