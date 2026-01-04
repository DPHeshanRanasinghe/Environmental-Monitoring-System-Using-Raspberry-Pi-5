# Environmental Monitoring System Using Raspberry Pi 5

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%205-red.svg)

A real-time weather monitoring and visualization system built with Raspberry Pi 5, Python, and Flask.

## Features

- **Live Weather Data Collection**: Fetches real-time weather data from OpenWeatherMap API
- **Historical Data Logging**: Stores temperature, humidity, and wind speed in CSV format
- **Data Visualization**: Generates beautiful matplotlib charts showing temperature trends
- **Web Dashboard**: Flask-based web interface with auto-refresh for live monitoring
- **SSH-Friendly**: Designed to run headless on Raspberry Pi via SSH

## Components

- `collector.py` - Fetches weather data from OpenWeatherMap API
- `analyzer.py` - Analyzes historical data and generates charts
- `dashboard.py` - Flask web server for visualization dashboard
- `run_all.sh` - Automation script to run the collection and analysis pipeline
- `web_check.py` - Utility script to verify internet connectivity

## Setup

### Prerequisites

- Raspberry Pi 5 (or any Raspberry Pi/Linux system)
- Python 3.7+
- OpenWeatherMap API Key (get one free at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/Environmental-Monitoring-System-Using-Raspberry-Pi-5.git
cd Environmental-Monitoring-System-Using-Raspberry-Pi-5
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install requests pandas matplotlib flask
```

4. Configure your API key:
   - Edit `collector.py` and replace `API_KEY` with your OpenWeatherMap API key
   - Optionally, set your preferred city in `CITY_NAME`

## Usage

### Manual Execution

1. **Collect data**:
```bash
python3 collector.py
```

2. **Generate charts**:
```bash
python3 analyzer.py
```

3. **Start web dashboard**:
```bash
python3 dashboard.py
```
Then access the dashboard at `http://[YOUR_PI_IP]:5000`

### Automated Execution

Run the complete pipeline:
```bash
bash run_all.sh
```

### Automation with Cron

To collect data automatically every hour:
```bash
crontab -e
```
Add this line:
```
0 * * * * /home/YOUR_USERNAME/path/to/run_all.sh
```

## Dashboard Access

Once the Flask server is running, access the dashboard from any device on your network:
- From the Pi: `http://localhost:5000`
- From another device: `http://[RASPBERRY_PI_IP]:5000`

The dashboard auto-refreshes every 60 seconds.

## Project Structure

```
Environmental_Monitor_Pi5/
├── collector.py          # Data collection module
├── analyzer.py           # Data analysis and visualization
├── dashboard.py          # Web dashboard server
├── run_all.sh           # Automation script
├── web_check.py         # Connectivity test utility
├── weather_history.csv  # Historical data log (generated)
└── temperature_chart.png # Generated chart (generated)
```

## Technologies Used

- **Python 3** - Core programming language
- **Requests** - HTTP library for API calls
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Chart generation
- **Flask** - Web framework for dashboard
- **OpenWeatherMap API** - Weather data source

## Future Enhancements

- [ ] Add humidity and wind speed visualizations
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Email/SMS alerts for extreme weather conditions
- [ ] Multiple location monitoring
- [ ] Historical data comparison
- [ ] Docker containerization

## Security Note

**Never commit your API keys to version control!** Use environment variables or a `.env` file for sensitive data.

## Author

**Heshan Ranasinghe**  
Electronic and Telecommunication Engineering Undergraduate

- Email: hranasinghe505@gmail.com
- GitHub: [@DPHeshanRanasinghe](https://github.com/DPHeshanRanasinghe)
- LinkedIn: [Heshan Ranasinghe](https://www.linkedin.com/in/heshan-ranasinghe-988b00290)

Developed on Raspberry Pi 5 via SSH

## Acknowledgments

- OpenWeatherMap for providing free weather data API
- Raspberry Pi Foundation for amazing hardware
