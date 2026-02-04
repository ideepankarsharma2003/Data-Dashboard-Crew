from crewai import Agent, Task, Crew, Process
from crewai_tools import CodeInterpreterTool

from config import agents, tasks    

python_interpreter = CodeInterpreterTool()

data_analyst = Agent(
    role=agents["data_analyst"]["role"],
    goal=agents["data_analyst"]["goal"],
    backstory=agents["data_analyst"]["backstory"],
    tools=[python_interpreter],
    verbose=True
)

formatter = Agent(
    role=agents["formatter"]["role"],
    goal=agents["formatter"]["goal"],
    backstory=agents["formatter"]["backstory"],
    verbose=True
)

analyze_task = Task(
    description=tasks["analyze_data_task"]["description"],
    expected_output=tasks["analyze_data_task"]["expected_output"],
    agent=data_analyst,
    tools=[python_interpreter]
)

format_task = Task(
    description=tasks["format_dashboard_task"]["description"],
    expected_output=tasks["format_dashboard_task"]["expected_output"],
    agent=formatter,
    output_file="dashboard.html"
)

crew = Crew(
    agents=[data_analyst, formatter],
    tasks=[analyze_task, format_task],
    process=Process.sequential
)
