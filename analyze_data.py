import numpy as np
import pandas as pd


def evaluate_vector_risk(row):
    # Vector Proliferation: Thrives in warm (20-30C) and humid (>70%) environments after rain
    # Using Open-Meteo column names: temperature_2m, relative_humidity_2m, precipitation
    if (
        (20 <= row["temperature_2m"] <= 30)
        and (row["relative_humidity_2m"] > 70)
        and (row["precipitation"] > 0)
    ):
        return "High Proliferation Risk (Optimal Vector Lifecycle)"
    elif (20 <= row["temperature_2m"] <= 30) and (
        row["relative_humidity_2m"] > 60
    ):
        return "Moderate Risk (Sustained Vector Activity)"
    else:
        return "Low Risk (Suppressed Vector Activity)"


def evaluate_genotoxic_stress(row):
    # Genotoxic Solar Stress: High UV index values flag accelerated DNA/cellular damage mechanics
    # Using Open-Meteo column name: uv_index
    if row["uv_index"] >= 8:
        return "Severe Stress (Upregulation of NER Pathways & Thymine Dimer Repair)"
    elif 3 <= row["uv_index"] < 8:
        return "Moderate Stress (Standard ROS Neutralization Active)"
    else:
        return "Baseline (Minimal Cellular Radiation Stress)"


def analyze_data():
    input_file = "clean_weather_data.csv"

    try:
        # Load the cleaned dataset
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(
            f"Error: {input_file} not found. Please run your cleaning script first."
        )
        return

    if df is None or df.empty:
        print("No data to analyze.")
        return

    # --- Homework 4 Standard Data Diagnostics ---
    print("==================================================")
    print("📋 DATASET DIAGNOSTICS")
    print("==================================================")

    print("Dataset shape:")
    print(df.shape)

    print("\nSummary statistics:")
    print(df.describe())

    print("\nCorrelation Matrix:")
    # Drop non-numeric columns like time string for correlation calculation
    print(df.corr(numeric_only=True))

    # --- Applying Your Custom Epidemiological and Molecular Logic ---
    print("\n==================================================")
    print("🔬 BIOLOGICAL AND EPIDEMIOLOGICAL ANALYSIS")
    print("==================================================")

    # Map the hourly weather rows to your custom biological indicators
    df["vector_epidemiology_status"] = df.apply(evaluate_vector_risk, axis=1)
    df["cellular_mutagenic_status"] = df.apply(
        evaluate_genotoxic_stress, axis=1
    )

    # Value Counts of Risks over the forecast window
    print("Vector Proliferation Risk Windows Detected (Hourly Intervals):")
    print(df["vector_epidemiology_status"].value_counts())

    print("\nCellular Genotoxic Stress Windows Detected (Hourly Intervals):")
    print(df["cellular_mutagenic_status"].value_counts())

    # Save these mapped indicators to a final file for plotting later
    output_file = "analyzed_epidemiology_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\nAnalysis complete! Mapped dataset saved to '{output_file}'")


if __name__ == "__main__":
    analyze_data()
