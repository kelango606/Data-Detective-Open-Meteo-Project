from fetch_data import fetch_api_data
from clean_data import clean_data
from analyze_data import analyze_data
from visualize_data import visualize_data

def main():
    # ----------------------------
    # Choose your API
    # ----------------------------
    urls = {
        "countries": "https://restcountries.com/v3.1/all",
        "open_meteo": "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&hourly=temperature_2m,precipitation",
        "world_bank": "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json",
        "nasa": "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"  # replace DEMO_KEY
    }
    
    chosen_api = "countries"  # TODO: choose one from the above list, or one of your own
    url = urls[chosen_api]
    
    # ----------------------------
    # 1. Fetch data
    # ----------------------------
    raw_data = fetch_api_data(url)
    
    # ----------------------------
    # 2. Clean data
    # ----------------------------
    cleaned_data = clean_data(raw_data)
    
    # ----------------------------
    # 3. Analyze data
    # ----------------------------
    analyze_data(cleaned_data)
    
    # ----------------------------
    # 4. Visualize data
    # ----------------------------
    visualize_data(cleaned_data)

if __name__ == "__main__":
    main()
