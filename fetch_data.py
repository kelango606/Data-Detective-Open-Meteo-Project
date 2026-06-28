import pandas as pd
import requests

def fetch_gfs_weather(lat, lon):
    print(f"Fetching weather data for Latitude: {lat}, Longitude: {lon}...")
    
    # Using the primary stable Open-Meteo endpoint with the GFS model specified as a parameter
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "models": "gfs_seamless", # Forces the exact GFS model data you want
        "hourly": "temperature_2m,relative_humidity_2m,precipitation,uv_index",
        "forecast_days": 7,
        "timezone": "auto"
    }
    
    # Adding a standard browser header so your local network/firewall safely passes the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # Send the request with the browser headers
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Parse data
        data = response.json()
        hourly_dict = data.get("hourly", {})
        df = pd.DataFrame(hourly_dict)
        
        # Save file
        df.to_csv("raw_weather_data.csv", index=False)
        print("🎉 Success! Raw data fetched and saved to 'raw_weather_data.csv'")
        print("\nFirst 3 rows of fetched data:")
        print(df.head(3))
        
    except Exception as e:
        print("\n❌ THE SCRIPT CRASHED BECAUSE OF THIS ERROR:")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {e}")

if __name__ == "__main__":
    # Example coordinates
    fetch_gfs_weather(lat=37.3382, lon=-121.8863)