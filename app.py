import streamlit as st
import os
import json
from datetime import datetime
import pandas as pd

# Import agent modules
from agents.outline_designer import OutlineDesigner
from agents.budget_estimator import BudgetEstimator
from agents.reviewer import ReviewerSimulation
from utils.memory import VersionTracker

# Set page configuration
st.set_page_config(
    page_title="AI-Powered Grant Proposal Assistant",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'current_proposal' not in st.session_state:
    st.session_state.current_proposal = {
        'topic': '',
        'goals': '',
        'funding_agency': '',
        'outline': '',
        'budget': {},
        'feedback': '',
        'version': 1,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if 'proposals' not in st.session_state:
    st.session_state.proposals = []

# Initialize version tracker
version_tracker = VersionTracker()

# Title and description
st.title("AI-Powered Grant Proposal Assistant")
st.markdown("""
This application helps researchers and nonprofits draft effective grant proposals using AI assistance.
Input your project details and use the different tools to develop your proposal.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Input Details", "Outline Designer", "Budget Estimator", "Reviewer Simulation"])

# Input Details Page
if page == "Input Details":
    st.header("Project Details")
    
    # Input form
    with st.form("project_details_form"):
        topic = st.text_input("Research/Project Topic", st.session_state.current_proposal['topic'])
        goals = st.text_area("Project Goals", st.session_state.current_proposal['goals'])
        funding_agency = st.text_input("Target Funding Agency", st.session_state.current_proposal['funding_agency'])
        additional_info = st.text_area("Additional Information (optional)")
        
        submitted = st.form_submit_button("Save Details")
        
        if submitted:
            st.session_state.current_proposal['topic'] = topic
            st.session_state.current_proposal['goals'] = goals
            st.session_state.current_proposal['funding_agency'] = funding_agency
            st.session_state.current_proposal['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save to version history
            version_tracker.save_version(st.session_state.current_proposal, "Updated project details")
            
            st.success("Project details saved successfully!")

# Outline Designer Page
elif page == "Outline Designer":
    st.header("Outline Designer")
    
    # Check if required fields are filled
    if not st.session_state.current_proposal['topic'] or not st.session_state.current_proposal['goals']:
        st.warning("Please fill in the project topic and goals in the Input Details page first.")
    else:
        st.write(f"Generating outline for: **{st.session_state.current_proposal['topic']}**")
        
        # Initialize outline designer agent
        outline_designer = OutlineDesigner()
        
        if st.button("Generate Outline"):
            with st.spinner("Generating outline..."):
                outline = outline_designer.generate_outline(
                    topic=st.session_state.current_proposal['topic'],
                    goals=st.session_state.current_proposal['goals'],
                    funding_agency=st.session_state.current_proposal['funding_agency']
                )
                
                st.session_state.current_proposal['outline'] = outline
                st.session_state.current_proposal['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Save to version history
                version_tracker.save_version(st.session_state.current_proposal, "Generated outline")
        
        # Display current outline if it exists
        if st.session_state.current_proposal['outline']:
            st.subheader("Generated Outline")
            st.write(st.session_state.current_proposal['outline'])
            
            # Allow editing
            edited_outline = st.text_area("Edit Outline", st.session_state.current_proposal['outline'], height=400)
            
            if st.button("Save Edited Outline"):
                st.session_state.current_proposal['outline'] = edited_outline
                st.session_state.current_proposal['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Save to version history
                version_tracker.save_version(st.session_state.current_proposal, "Edited outline")
                
                st.success("Outline saved successfully!")

# Budget Estimator Page
elif page == "Budget Estimator":
    st.header("Budget Estimator")
    
    # Check if required fields are filled
    if not st.session_state.current_proposal['topic'] or not st.session_state.current_proposal['goals']:
        st.warning("Please fill in the project topic and goals in the Input Details page first.")
    else:
        st.write(f"Estimating budget for: **{st.session_state.current_proposal['topic']}**")
        
        # Initialize budget estimator agent
        budget_estimator = BudgetEstimator()
        
        # Input for budget parameters
        project_duration = st.slider("Project Duration (months)", 1, 60, 12)
        team_size = st.slider("Team Size (people)", 1, 20, 3)
        
        if st.button("Generate Budget Estimate"):
            with st.spinner("Estimating budget..."):
                budget = budget_estimator.estimate_budget(
                    topic=st.session_state.current_proposal['topic'],
                    goals=st.session_state.current_proposal['goals'],
                    funding_agency=st.session_state.current_proposal['funding_agency'],
                    duration=project_duration,
                    team_size=team_size
                )
                
                st.session_state.current_proposal['budget'] = budget
                st.session_state.current_proposal['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Save to version history
                version_tracker.save_version(st.session_state.current_proposal, "Generated budget estimate")
        
        # Display current budget if it exists
        if st.session_state.current_proposal.get('budget'):
            st.subheader("Budget Estimate")
            
            # Convert budget to DataFrame for display
            budget_df = pd.DataFrame(st.session_state.current_proposal['budget'].items(), columns=['Category', 'Amount (USD)'])
            
            # Add INR column (using conversion rate of 1 USD = 75 INR)
            budget_df['Amount (INR)'] = budget_df['Amount (USD)'].apply(lambda x: x * 75)
            
            # Format the currency values
            budget_df['Amount (USD)'] = budget_df['Amount (USD)'].apply(lambda x: f"${x:,.2f}")
            budget_df['Amount (INR)'] = budget_df['Amount (INR)'].apply(lambda x: f"₹{x:,.2f}")
            
            st.table(budget_df)
            
            # Display total in both currencies
            total_usd = sum(st.session_state.current_proposal['budget'].values())
            total_inr = total_usd * 75
            st.write(f"**Total Budget: ${total_usd:,.2f} (₹{total_inr:,.2f})**")
            
            # Allow downloading budget as CSV
            # Create a copy of the DataFrame with numeric values for CSV export
            export_df = pd.DataFrame(st.session_state.current_proposal['budget'].items(), columns=['Category', 'Amount (USD)'])
            export_df['Amount (INR)'] = export_df['Amount (USD)'] * 75
            csv = export_df.to_csv(index=False)
            
            st.download_button(
                label="Download Budget as CSV",
                data=csv,
                file_name="budget_estimate.csv",
                mime="text/csv"
            )

# Reviewer Simulation Page
elif page == "Reviewer Simulation":
    st.header("Reviewer Simulation")
    
    # Check if required fields are filled
    if not st.session_state.current_proposal['outline']:
        st.warning("Please generate an outline in the Outline Designer page first.")
    else:
        st.write("Simulating reviewer feedback for your proposal")
        
        # Initialize reviewer simulation agent
        reviewer = ReviewerSimulation()
        
        if st.button("Generate Reviewer Feedback"):
            with st.spinner("Generating feedback..."):
                feedback = reviewer.generate_feedback(
                    topic=st.session_state.current_proposal['topic'],
                    goals=st.session_state.current_proposal['goals'],
                    funding_agency=st.session_state.current_proposal['funding_agency'],
                    outline=st.session_state.current_proposal['outline'],
                    budget=st.session_state.current_proposal.get('budget', {})
                )
                
                st.session_state.current_proposal['feedback'] = feedback
                st.session_state.current_proposal['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Save to version history
                version_tracker.save_version(st.session_state.current_proposal, "Generated reviewer feedback")
        
        # Display current feedback if it exists
        if st.session_state.current_proposal.get('feedback'):
            st.subheader("Reviewer Feedback")
            st.write(st.session_state.current_proposal['feedback'])

# Footer
st.markdown("---")