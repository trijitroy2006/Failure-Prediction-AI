import streamlit as st
import pandas as pd
import market_analysis

st.set_page_config(page_title="Failure Prediction AI", layout="wide")

st.title("Failure Prediction AI")
st.subheader("Milestone 1: Data Collection & Market Intelligence")

tab1, tab2 = st.tabs(["Project Input", "Market Intelligence"])

with tab1:
    st.header("Project Configuration")
    st.write("Enter your project details below to generate automated market insights.")
    
    with st.form("project_form"):
        startup_name = st.text_input("Startup / Project Name", "Nexus Dynamics")
        industry = st.selectbox("Industry / Sector", ["Technology", "Healthcare", "Finance", "Education"])
        business_model = st.selectbox("Business Model", ["SaaS", "B2B", "B2C", "Marketplace"])
        
        col1, col2 = st.columns(2)
        with col1:
            target_market = st.text_input("Target Market Demographic", "SMBs")
        with col2:
            budget = st.number_input("Initial Budget (USD)", min_value=0, value=150000, step=10000)
            
        description = st.text_area("Project Description", "Provide a brief overview of your product or service...")
        
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
        st.success("Project data submitted successfully! Navigate to the 'Market Intelligence' tab to view results.")

with tab2:
    st.header("Market Analysis & Competitor Landscape")
    
    if 'project_data' in st.session_state:
        data = st.session_state['project_data']
        
        st.write(f"### Project: {data['startup_name']}")
        
        # Get Market Data from the existing market_analysis.py logic
        m_data = market_analysis.get_market_data(data['industry'], data['target_market'], data['budget'])
        
        st.subheader("Market Sizing (AI Estimates)")
        m_col1, m_col2, m_col3 = st.columns(3)
        
        m_col1.metric("TAM (Total Addressable Market)", m_data['TAM']['value'], m_data['TAM']['growth'])
        m_col2.metric("SAM (Serviceable Addressable)", m_data['SAM']['value'], m_data['SAM']['growth'])
        m_col3.metric("SOM (Serviceable Obtainable)", m_data['SOM']['value'], m_data['SOM']['growth'])
        
        st.markdown("---")
        
        st.subheader("Competitor Landscape")
        c_data = market_analysis.get_competitor_data(data['startup_name'], data['industry'], data['business_model'])
        
        # Display as a dataframe
        df_competitors = pd.DataFrame(c_data)
        st.dataframe(df_competitors, use_container_width=True)
        
        st.subheader("Market Trend Simulation")
        # Creating a simple trend chart using st.line_chart
        chart_data = pd.DataFrame(
            [30, 45, 52, 65, 78, 90, 100],
            columns=["Market Projection"],
            index=["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
        )
        st.line_chart(chart_data)
        
    else:
        st.info("ℹ️ Please submit your project configuration in the 'Project Input' tab first.")
