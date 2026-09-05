import streamlit as st
import pandas as pd
import market_analysis
import risk_analysis

st.set_page_config(page_title="Failure Prediction AI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("### ▲ MILESTONE 2 • WEEKS 3–4")
st.title("Risk Assessment & SWOT Analysis")
st.write("AI-powered risk scoring and strategic evaluation")

tab1, tab2, tab3, tab4 = st.tabs(["Project Input", "Risk Assessment", "Recommendations", "Dash"])

with tab1:
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

with tab2:
    if 'project_data' in st.session_state:
        data = st.session_state['project_data']
        scores = risk_analysis.calculate_risk_scores(data)
        swot = risk_analysis.generate_swot(data)
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.subheader("RISK SCORE")
            st.metric("Success Probability", f"{scores['overall_success_probability']}%")
            st.write(f"**{scores['risk_level'].upper()} RISK**")
            
            st.write("---")
            st.write("**Key Risks**")
            st.progress(scores['financial_risk'] / 100, text="Financial Risk")
            st.progress(scores['market_risk'] / 100, text="Market Risk")
            st.progress(scores['technical_risk'] / 100, text="Technical Risk")
            st.progress(scores['operational_risk'] / 100, text="Operational Risk")

        with c2:
            st.subheader("SWOT ANALYSIS")
            st.success("**Strengths**\n" + "\n".join([f"- {s}" for s in swot['Strengths']]))
            st.error("**Weaknesses**\n" + "\n".join([f"- {w}" for w in swot['Weaknesses']]))
            st.info("**Opportunities**\n" + "\n".join([f"- {o}" for o in swot['Opportunities']]))
            st.warning("**Threats**\n" + "\n".join([f"- {t}" for t in swot['Threats']]))

        with c3:
            st.subheader("FEASIBILITY")
            st.metric("Feasibility Score", f"{scores['overall_success_probability'] + 7}%")
            
            st.write("---")
            st.write("**Assessment Metrics**")
            # Using disabled sliders to represent AI-determined feasibility metrics visually
            market_opp = 80 if data['industry'] == 'Technology' else 65
            team_cap = 70 if data['budget'] > 50000 else 40
            comp_adv = 60
            res_avail = 90 if data['budget'] > 200000 else 50
            
            st.slider("Market Opportunity", 0, 100, market_opp, disabled=True)
            st.slider("Team Capability", 0, 100, team_cap, disabled=True)
            st.slider("Competitive Advantage", 0, 100, comp_adv, disabled=True)
            st.slider("Resource Availability", 0, 100, res_avail, disabled=True)
            
    else:
        st.info("Please submit a project in the 'Project Input' tab first.")

with tab3:
    st.subheader("Recommendations")
    st.info("AI-powered mitigation strategies will be available in Milestone 3.")

with tab4:
    st.subheader("Dashboard (Market Intelligence)")
    if 'project_data' in st.session_state:
        data = st.session_state['project_data']
        m_data = market_analysis.get_market_data(data['industry'], data['target_market'], data['budget'])
        
        m1, m2, m3 = st.columns(3)
        m1.metric("TAM", m_data['TAM']['value'], m_data['TAM']['growth'])
        m2.metric("SAM", m_data['SAM']['value'], m_data['SAM']['growth'])
        m3.metric("SOM", m_data['SOM']['value'], m_data['SOM']['growth'])
        
        st.write("---")
        st.subheader("Competitor Landscape")
        c_data = market_analysis.get_competitor_data(data['startup_name'], data['industry'], data['business_model'])
        
        # Display as a dataframe
        df_competitors = pd.DataFrame(c_data)
        st.dataframe(df_competitors, width='stretch')
        
    else:
        st.info("Submit a project idea to view market dashboard.")
