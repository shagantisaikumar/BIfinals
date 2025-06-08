import requests
import psycopg2

API_KEY = "rR4ksB8TNlrFxfJOtDceGlt6TGJ0vHXn6FLY0k0v"
URL = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-06-01&end_date=2024-06-07&api_key={API_KEY}"
DB_PARAMS = {
    "host": "localhost",
    "database": "nasa_db",
    "user": "postgres",
    "password": "Pulla@12345"  # Change this
}

def fetch_data():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    neos = []

    for date in data['near_earth_objects']:
        for item in data['near_earth_objects'][date]:
            neos.append({
                "id": item["id"],
                "name": item["name"],
                "absolute_magnitude": item["absolute_magnitude_h"],
                "is_potentially_hazardous": item["is_potentially_hazardous_asteroid"],
                "estimated_diameter_min": item["estimated_diameter"]["kilometers"]["estimated_diameter_min"],
                "estimated_diameter_max": item["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
                "close_approach_date": item["close_approach_data"][0]["close_approach_date"],
                "relative_velocity_km_s": item["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"],
                "miss_distance_km": item["close_approach_data"][0]["miss_distance"]["kilometers"],
                "orbiting_body": item["close_approach_data"][0]["orbiting_body"]
            })
            if len(neos) >= 40:
                return neos
    return neos

def load_to_postgres(neos):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS nasa_asteroids (
            id TEXT PRIMARY KEY,
            name TEXT,
            absolute_magnitude FLOAT,
            is_potentially_hazardous BOOLEAN,
            diameter_min_km FLOAT,
            diameter_max_km FLOAT,
            close_approach_date DATE,
            relative_velocity_km_s FLOAT,
            miss_distance_km FLOAT,
            orbiting_body TEXT
        );
    """)
    for neo in neos:
        cur.execute("""
            INSERT INTO nasa_asteroids VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            neo["id"],
            neo["name"],
            neo["absolute_magnitude"],
            neo["is_potentially_hazardous"],
            neo["estimated_diameter_min"],
            neo["estimated_diameter_max"],
            neo["close_approach_date"],
            float(neo["relative_velocity_km_s"]),
            float(neo["miss_distance_km"]),
            neo["orbiting_body"]
        ))
    conn.commit()
    cur.close()
    conn.close()

def main():
    print("Fetching NASA data...")
    data = fetch_data()
    print(f"Loaded {len(data)} records.")
    load_to_postgres(data)
    print("Data loaded to PostgreSQL.")

if __name__ == "__main__":
    main()
