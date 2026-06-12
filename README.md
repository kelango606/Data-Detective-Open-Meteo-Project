# Public API Data Project

## Overview
This project demonstrates how to retrieve, clean, analyze, and visualize data from public APIs using Python.

Students can choose one of the following APIs:

- **Countries**: https://restcountries.com/
- **Open-Meteo**: https://open-meteo.com/
- **World Bank**: https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
- **NASA**: https://api.nasa.gov/ (requires free API key via email)

---

## Project Structure

    project/
    │
    ├── fetch_data.py        # Fetch data from API
    ├── clean_data.py        # Clean and preprocess data
    ├── analyze_data.py      # Analyze the data
    ├── visualize_data.py    # Visualize the data
    ├── main.py              # Main workflow
    └── README.md            # Project instructions

---

## Notes

- **Countries, Open-Meteo, and World Bank APIs do not require authentication or API keys.**
- **NASA API requires a free API key.**  
  Sign up with your email at https://api.nasa.gov/. Your API key will be sent to you by email.

---

## Instructions

1. Update `main.py` with the API you want to use.
2. Run `main.py` to fetch data from the API.
3. Implement the following functions in their respective files:
   - `fetch_data()` in **fetch_data.py**
   - `clean_data()` in **clean_data.py**
   - `analyze_data()` in **analyze_data.py**
   - `visualize_data()` in **visualize_data.py**
4. Use Python libraries such as **pandas**, **matplotlib**, or **seaborn** to complete the later steps of the project.