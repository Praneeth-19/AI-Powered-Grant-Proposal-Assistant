# AI-Powered Grant Proposal Assistant

## Overview
A Streamlit-based application that helps researchers and organizations create grant proposals using AI assistance. The application provides intelligent tools for outline generation, budget estimation (in USD and INR), and simulated reviewer feedback.

## Features
- **Project Details Input**: Enter your project topic, goals, and target funding agency
- **Outline Designer**: AI-powered outline generation based on your project details
- **Budget Estimator**: 
  - Generate detailed budget estimates
  - Support for both USD and INR currencies
  - Customizable project duration and team size
- **Reviewer Simulation**: Get AI-simulated feedback on your proposal

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Project Structure
AI-Powered Grant Proposal Assistant/
├── agents/
│   ├── budget_estimator.py   # Budget estimation logic
│   ├── outline_designer.py   # Outline generation
│   └── reviewer.py          # Reviewer simulation
├── utils/
│   └── memory.py           # Data persistence
├── app.py                  # Main Streamlit application
└── requirements.txt        # Python dependencies


## How to Use

1. **Input Project Details**
   - Enter your project topic
   - Define project goals
   - Specify target funding agency

2. **Generate Outline**
   - Click "Generate Outline" to create a structured proposal outline
   - Edit the generated outline as needed

3. **Estimate Budget**
   - Enter project duration and team size
   - Get budget estimates in both USD and INR
   - Download budget details as CSV

4. **Get Reviewer Feedback**
   - Submit your proposal for AI review
   - Receive feedback on strengths and potential improvements