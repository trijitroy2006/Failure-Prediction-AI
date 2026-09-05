import streamlit as st
import pandas as pd
import market_analysis

st.set_page_config(page_title="Failure Prediction AI", layout="wide")

# Header matching the PDF
st.markdown("### ▲ MILESTONE 1 • WEEKS 1-2")
st.title("Data Collection & Market Intelligence")
st.write("Gather project data and analyze market landscape")

# Tabs exactly like the PDF
st.tabs(["Project Input", "Risk Assessment", "Recommendations", "Dashboard"])

# 3-Column Layout exactly like the PDF
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
