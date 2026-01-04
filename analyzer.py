# analyzer.py - Reads the data, processes it, and creates a chart.

import pandas as pd
import matplotlib.pyplot as plt
import os

HISTORY_FILE = 'weather_history.csv'
CHART_FILE = 'temperature_chart.png'

def analyze_and_plot():
    """Reads historical data, calculates metrics, and generates a temperature plot."""
    print("\n--- Starting Data Analysis and Plotting ---")
    
    if not os.path.exists(HISTORY_FILE):
        print(f"Error: '{HISTORY_FILE}' not found. Please run collector.py first.")
        return

    try:
        # 1. Load the data from the CSV file
        df = pd.read_csv(HISTORY_FILE)
        
        # 2. Data Processing: Convert the readable time column to datetime objects
        df['time_readable'] = pd.to_datetime(df['time_readable'])
        
        # 3. Data Analysis: Calculate the average temperature
        avg_temp = df['temperature_c'].mean()
        
        print(f"Total data points analyzed: {len(df)}")
        print(f"Average Temperature: {avg_temp:.2f}°C")
        
        # 4. Data Visualization: Create a time-series plot
        
        # Use a non-interactive backend for plotting over SSH/CLI
        plt.switch_backend('agg') 
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['time_readable'], df['temperature_c'], marker='o', linestyle='-', color='red', label='Current Temperature')
        
        # Add a baseline for context
        plt.axhline(avg_temp, color='blue', linestyle='--', label=f'Overall Average ({avg_temp:.2f}°C)')

        plt.title('Local Temperature Trend (The Heartbeat of Our Environment)')
        plt.xlabel('Time of Observation')
        plt.ylabel('Temperature (°C)')
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()
        
        # 5. Save the chart as an image file
        plt.savefig(CHART_FILE)
        print(f"SUCCESS: Chart saved as '{CHART_FILE}'")

    except Exception as e:
        print(f"An error occurred during analysis or plotting: {e}")

if __name__ == "__main__":
    analyze_and_plot()
    print("\n--- Analysis Finished ---")
