import streamlit as st
import pages.dashboard as dashboard
import pages.safety_analyzer as safety_analyzer
import pages.productivity_reporter as productivity_reporter
import pages.material_estimator as material_estimator
import pages.schedule_optimizer as schedule_optimizer
import pages.floor_plan_visualizer as floor_plan_visualizer

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
    dashboard.app()

elif page == "Safety Analyzer":
    safety_analyzer.app()

elif page == "Productivity Reporter":
    productivity_reporter.app()

elif page == "Material Estimator":
    material_estimator.app()

elif page == "Schedule Optimizer":
    schedule_optimizer.app()

elif page == "Floor Plan Visualizer":
    floor_plan_visualizer.app()
