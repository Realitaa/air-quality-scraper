from datetime import datetime, timezone, timedelta
import time
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

LAT = os.getenv("LAT")
LON = os.getenv("LON")

BASE_URL = "https://api.openweathermap.org/data/2.5/air_pollution/history"

# Data historical tersedia sejak 27 November 2020
START_DATE = datetime(2020, 11, 27, tzinfo=timezone.utc)
END_DATE = datetime.now(timezone.utc)

# Ambil data per 30 hari untuk menghindari request terlalu besar
CHUNK_DAYS = 30


def fetch_chunk(start_ts: int, end_ts: int):
    params = {
        "lat": LAT,
        "lon": LON,
        "start": start_ts,
        "end": end_ts,
        "appid": API_KEY,
    }

    response = requests.get(BASE_URL, params=params, timeout=60)
    response.raise_for_status()

    return response.json().get("list", [])


def main():
    all_rows = []

    current_start = START_DATE

    while current_start < END_DATE:
        current_end = min(
            current_start + timedelta(days=CHUNK_DAYS),
            END_DATE
        )

        print(
            f"Fetching {current_start:%Y-%m-%d} "
            f"-> {current_end:%Y-%m-%d}"
        )

        records = fetch_chunk(
            int(current_start.timestamp()),
            int(current_end.timestamp())
        )

        for item in records:
            row = {
                "timez": datetime.fromtimestamp(
                    item["dt"],
                    tz=timezone.utc
                ).isoformat()
            }

            row.update(item["components"])

            all_rows.append(row)

        current_start = current_end

        # Hindari rate limit
        time.sleep(1)

    df = pd.DataFrame(all_rows)

    df.sort_values("timez", inplace=True)

    output_file = f"output/air_pollution_history_{LAT}_{LON}.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved {len(df)} rows to {output_file}")


if __name__ == "__main__":
    main()