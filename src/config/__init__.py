import os
import yaml

# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct paths to the YAML files
agents_path = os.path.join(current_dir, 'agents.yaml')
tasks_path = os.path.join(current_dir, 'tasks.yaml')

# Load the agents configuration
if os.path.exists(agents_path):
    with open(agents_path, 'r') as f:
        agents = yaml.safe_load(f)
else:
    agents = {}

# Load the tasks configuration
if os.path.exists(tasks_path):
    with open(tasks_path, 'r') as f:
        tasks = yaml.safe_load(f)
else:
    tasks = {}
