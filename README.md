# Data Dashboard Crew

This project is an automated data analysis and dashboard generation system built using **CrewAI**. It leverages intelligent agents to analyze CSV data and create visually appealing, interactive HTML dashboards based on natural language queries.

## 🚀 Key Features

*   **Automated Data Analysis**: A Senior Data Analyst agent inspects CSV files, performs statistical analysis using Python, and extracts key insights.
*   **Natural Language Querying**: Users can ask questions about their data in plain English (e.g., "Visualize the portfolio performance for Garfield").
*   **Interactive Dashboards**: A Formatter agent converts the analytical results into a standalone HTML file featuring interactive charts powered by **Chart.js**.

## 🤖 Agents & Tasks

The crew consists of two main agents:

1.  **Senior Data Analyst**:
    *   **Goal**: Analyze CSV data and return structured JSON insights.
    *   **Tools**: Uses a Python Interpreter to execute data analysis code.
    *   **Task**: Receives a CSV path and a user query, processes the data, and outputs JSON containing summaries, tables, and chart specifications.

2.  **Dashboard Designer (Formatter)**:
    *   **Goal**: Create a visual dashboard from structured data.
    *   **Task**: Takes the JSON output from the analyst and generates a `dashboard.html` file with a clean layout and interactive visualizations.

## 🛠️ Installation

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    Ensure you have Python >= 3.13. Install the required packages using pip:

    ```bash
    pip install crewai crewai-tools pandas
    ```

    *Check `pyproject.toml` for the full dependency list.*

3.  **Environment Setup**:
    Make sure you have your environment variables set up (e.g., `OPENAI_API_KEY`) as CrewAI relies on LLMs. Create a `.env` file in the root directory if needed.

## 🏃 Usage

1.  **Prepare your data**:
    Place your CSV file in `src/data/`. The default example uses `src/data/holdings.csv`.

2.  **Configure the Query**:
    Open `src/main.py` and modify the `inputs` dictionary to match your query and file path:

    ```python
    inputs={
        "query": "Your question here...",
        "csv_path": "src/data/your_file.csv"
    }
    ```

3.  **Run the Crew**:
    Execute the main script:

    ```bash
    python src/main.py
    ```

4.  **View Output**:
    Once the process completes, open the generated **`dashboard.html`** file in your web browser to view the results.

    <img width="600" alt="image" src="https://github.com/user-attachments/assets/759cc2e1-7b7e-467f-90a2-a209b05ac1cf" />


## 📂 Project Structure

```
data_dashboard_crew/
├── src/
│   ├── config/
│   │   ├── agents.yaml      # Agent definitions
│   │   └── tasks.yaml       # Task definitions
│   ├── data/
│   │   └── holdings.csv     # Example data
│   ├── crew.py              # Crew orchestration logic
│   └── main.py              # Entry point to run the crew
├── dashboard.html           # Generated output
├── pyproject.toml           # Project dependencies
└── README.md                # Documentation
```
