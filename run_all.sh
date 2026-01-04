#!/bin/bash

# --- Configuration ---
# Set the working directory to your project folder
cd /home/heshan/Documents/Projects/Python

# 1. Activate the Virtual Environment
source venv/bin/activate

# 2. Run the Data Collector
echo "Running collector.py at $(date)"
python3 collector.py

# 3. Run the Analyzer and update the chart
echo "Running analyzer.py at $(date)"
python3 analyzer.py

# 4. Deactivate the Virtual Environment (optional, but good practice)
deactivate
