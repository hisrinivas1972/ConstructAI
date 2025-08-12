import streamlit as st

st.set_page_config(page_title="ConstructAI", layout="wide")

st.title("🏗️ ConstructAI")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Safety Analyzer",
    "Productivity Reporter",
    "Material Estimator",
    "Schedule Optimizer",
    "Floor Plan Visualizer"
])

if page == "Dashboard":
    import pages.1_dashboard as dashboard
    dashboard.app()

elif page == "Safety Analyzer":
    import pages.2_safety_analyzer as safety
    safety.app()

elif page == "Productivity Reporter":
    import pages.3_productivity_reporter as productivity
    productivity.app()

elif page == "Material Estimator":
    import pages.4_material_estimator as material
    material.app()

elif page == "Schedule Optimizer":
    import pages.5_schedule_optimizer as schedule
    schedule.app()

elif page == "Floor Plan Visualizer":
    import pages.6_floor_plan_visualizer as floorplan
    floorplan.app()
