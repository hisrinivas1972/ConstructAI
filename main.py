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
    import pages.dashboard as dashboard
    dashboard.app()

elif page == "Safety Analyzer":
    import pages.safety_analyzer as safety
    safety.app()

elif page == "Productivity Reporter":
    import pages.productivity_reporter as productivity
    productivity.app()

elif page == "Material Estimator":
    import pages.material_estimator as material
    material.app()

elif page == "Schedule Optimizer":
    import pages.schedule_optimizer as schedule
    schedule.app()

elif page == "Floor Plan Visualizer":
    import pages.floor_plan_visualizer as floorplan
    floorplan.app()
