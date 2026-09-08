import streamlit as st
import pandas as pd
import market_analysis
import risk_analysis

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

st.title("Failure Prediction AI")
st.write("Intelligent decision-support platform to predict failure risks and recommend mitigations.")

tab_m1, tab_m2 = st.tabs(["Milestone 1: Market Intelligence", "Milestone 2: Risk Assessment"])

with tab_m1:
    st.markdown("### ▲ MILESTONE 1 • WEEKS 1-2")
    st.markdown("#### Data Collection & Market Intelligence")
    
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

with tab_m2:
    st.markdown("### ▲ MILESTONE 2 • WEEKS 3-4")
    st.markdown("#### Risk Assessment & SWOT Analysis")
    
    if 'project_data' in st.session_state:
        data = st.session_state['project_data']
        scores = risk_analysis.calculate_risk_scores(data)
        swot = risk_analysis.generate_swot(data)
        
        r_col1, r_col2, r_col3 = st.columns(3)
        
        with r_col1:
            st.subheader("RISK SCORE")
            st.metric("Success Probability", f"{scores['overall_success_probability']}%")
            st.write(f"**{scores['risk_level'].upper()} RISK**")
            
            st.write("---")
            st.write("**Key Risks**")
            st.progress(scores['financial_risk'] / 100, text="Financial Risk")
            st.progress(scores['market_risk'] / 100, text="Market Risk")
            st.progress(scores['technical_risk'] / 100, text="Technical Risk")
            st.progress(scores['operational_risk'] / 100, text="Operational Risk")

        with r_col2:
            st.subheader("SWOT ANALYSIS")
            st.success("**Strengths**\n" + "\n".join([f"- {s}" for s in swot['Strengths']]))
            st.error("**Weaknesses**\n" + "\n".join([f"- {w}" for w in swot['Weaknesses']]))
            st.info("**Opportunities**\n" + "\n".join([f"- {o}" for o in swot['Opportunities']]))
            st.warning("**Threats**\n" + "\n".join([f"- {t}" for t in swot['Threats']]))

        with r_col3:
            st.subheader("FEASIBILITY")
            st.metric("Feasibility Score", f"{scores['overall_success_probability'] + 7}%")
            
            st.write("---")
            st.write("**Assessment Metrics**")
            market_opp = 80 if data['industry'] == 'Technology' else 65
            team_cap = 70 if data['budget'] > 50000 else 40
            comp_adv = 60
            res_avail = 90 if data['budget'] > 200000 else 50
            
            st.slider("Market Opportunity", 0, 100, market_opp, disabled=True)
            st.slider("Team Capability", 0, 100, team_cap, disabled=True)
            st.slider("Competitive Advantage", 0, 100, comp_adv, disabled=True)
            st.slider("Resource Availability", 0, 100, res_avail, disabled=True)
            
    else:
        st.info("Please submit a project in the 'Milestone 1' tab first.")
