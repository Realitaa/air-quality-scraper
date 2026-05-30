# Air Quality Scraper

A simple Python script to collect historical air pollution data from the OpenWeather Air Pollution API and export it into a CSV file for further analysis.

## Features

* Fetches historical air quality data from OpenWeather.
* Supports any geographic location using latitude and longitude coordinates.
* Downloads data in 30-day chunks to avoid oversized requests.
* Exports results into CSV format.
* Uses environment variables for configuration.

## Tech Stack

* Python 3.12+
* uv Python Environment Manager
* Requests
* Pandas
* Python Dotenv
* OpenWeather Air Pollution API

## Project Structure

```text
.
├── .env.example
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Requirements

* Python 3.12 or newer
* OpenWeather API Key

## Installation

Clone the repository:

```bash
git clone https://github.com/Realitaa/air-quality-scraper.git
cd air-quality-scraper
```

Install dependencies using uv:

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file based on `.env.example`.

Example:

```env
API_KEY=your_openweather_api_key
LAT=3.6721858545325534
LON=98.68197158074453
```

### Environment Variables

| Variable | Description          |
| -------- | -------------------- |
| API_KEY  | OpenWeather API key  |
| LAT      | Latitude coordinate  |
| LON      | Longitude coordinate |

## Usage

Run the script:

```bash
python main.py
```

The script will:

1. Request historical air pollution data from OpenWeather.
2. Fetch data in 30-day intervals.
3. Merge all records into a single dataset.
4. Export the result as a CSV file.

Example output:

```text
Fetching 2020-11-27 -> 2020-12-27
Fetching 2020-12-27 -> 2021-01-26
...
Saved 47598 rows to output/air_pollution_history_3.6721858545325534_98.68197158074453.csv
```

## Output

Generated files are saved in:

```text
output/
```

Example:

```text
output/air_pollution_history_3.6721858545325534_98.68197158074453.csv
```

CSV columns include:

* timez
* co
* no
* no2
* o3
* so2
* pm2_5
* pm10
* nh3

## Data Source

This project uses:

* OpenWeather Air Pollution History API

Documentation:

https://openweathermap.org/api/air-pollution#history

## Notes

* Historical data availability depends on OpenWeather.
* Large date ranges may take several minutes to complete.
* The script includes a delay between requests to reduce the risk of rate limiting.

## License

MIT License
