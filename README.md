# AI-Powered Grant Proposal Assistant

## Project Overview

This AI-Powered Grant Proposal Assistant is a Streamlit-based application designed to help researchers, academics, and non-profit organizations streamline the grant proposal writing process. It leverages various AI agents to assist with outlining, budget estimation, and even simulating reviewer feedback, making the proposal development more efficient and effective.

## Features

- **Input Details**: Easily input and manage core project information such as topic, goals, and target funding agency.
- **Outline Designer**: Generate a structured proposal outline based on your project details, providing a solid starting point for your writing.
- **Budget Estimator**: Get an estimated budget breakdown for your project, with support for both USD and INR currencies.
- **Reviewer Simulation**: Receive simulated feedback from an AI reviewer, highlighting potential strengths, weaknesses, and suggestions for improvement before submission.
- **Version Tracking**: (Removed as per user request)

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd AI-Powered-Grant-Proposal-Assistant
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit application, execute the following command in your terminal from the project's root directory:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Project Structure
AI-Powered Grant Proposal Assistant/
├── agents/
│   ├── init .py
│   ├── budget_estimator.py
│   ├── outline_designer.py
│   └── reviewer.py
├── utils/
│   ├── init .py
│   └── memory.py
├── app.py
├── requirements.txt
└── README.md


-   `app.py`: The main Streamlit application file, handling UI and orchestrating agent interactions.
-   `agents/`: Contains individual AI agent modules.
    -   `outline_designer.py`: Generates proposal outlines.
    -   `budget_estimator.py`: Estimates project budgets.
    -   `reviewer.py`: Simulates reviewer feedback.
-   `utils/`: Contains utility functions and classes.
    -   `memory.py`: Handles version tracking and proposal memory (though version history is removed from UI).
-   `requirements.txt`: Lists all Python dependencies required to run the application.
-   `README.md`: This file, providing an overview of the project.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open-source and available under the MIT License.