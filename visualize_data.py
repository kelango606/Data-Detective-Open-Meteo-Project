# Reference Framework: matplotlib.pyplot implementation upgraded to interactive Plotly engine per project criteria.
import os
import webbrowser
import pandas as pd

# Safely verify/install Plotly inside the current local runtime environment
try:
    import plotly.express as px
    import plotly.graph_objects as go
except ImportError:
    import subprocess
    import sys
    print("📦 Plotly not detected. Launching automatic pip environment installation...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
    import plotly.express as px
    import plotly.graph_objects as go

def run_vs_code_dashboard():
    input_file = "analyzed_epidemiology_data.csv"
    
    # 1. Load the localized epidemiological dataset
    if not os.path.exists(input_file):
        print(f"❌ Error: '{input_file}' not found in the current working directory.")
        print("Please ensure you have run your 'analyze_data.py' script first.")
        return
        
    df = pd.read_csv(input_file)
    df["time"] = pd.to_datetime(df["time"])
    print("🔬 Mapped data ingested successfully! Generating interactive visualization HTML files...")

    # Create a subfolder to keep your VS Code directory perfectly organized
    output_dir = "dashboard_plots"
    os.makedirs(output_dir, exist_ok=True)
    
    generated_files = []

    # ==========================================
    # CHART 1: LINE GRAPH (Solar Stress Over Time)
    # ==========================================
    fig_line = px.line(
        df, x="time", y="uv_index", color="cellular_mutagenic_status",
        title="<b>Figure 1: Chronological Timeline of Genotoxic Solar Radiative Stress</b>",
        labels={"time": "Forecast Timeline", "uv_index": "UV Index Value", "cellular_mutagenic_status": "Molecular Response Phase"},
        color_discrete_map={
            "Severe Stress (Upregulation of NER Pathways & Thymine Dimer Repair)": "#EF553B", # Deep Crimson Red
            "Moderate Stress (Standard ROS Neutralization Active)": "#FECB52",               # Amber Gold
            "Baseline (Minimal Cellular Radiation Stress)": "#636EFA"                        # Cool Cobalt Blue
        },
        template="plotly_dark"
    )
    fig_line.update_layout(hovermode="x unified")
    path_line = os.path.join(output_dir, "1_line_solar_stress.html")
    fig_line.write_html(path_line)
    generated_files.append(path_line)

    # ==========================================
    # CHART 2: BAR GRAPH (Vector Proliferation Windows)
    # ==========================================
    vector_counts = df["vector_epidemiology_status"].value_counts().reset_index()
    vector_counts.columns = ["Risk Status", "Hourly Window Count"]
    
    fig_bar = px.bar(
        vector_counts, x="Risk Status", y="Hourly Window Count", color="Risk Status",
        title="<b>Figure 2: Distribution of Vector Proliferation Risk Windows</b>",
        labels={"Risk Status": "Epidemiological State", "Hourly Window Count": "Cumulative Hours Exposed"},
        color_discrete_map={
            "High Proliferation Risk (Optimal Vector Lifecycle)": "#FF6692", # Vibrant Rose Pink
            "Moderate Risk (Sustained Vector Activity)": "#B6E880",           # Light Sage Green
            "Low Risk (Suppressed Vector Activity)": "#19D3F3"               # Electric Cyan
        },
        template="plotly_dark"
    )
    path_bar = os.path.join(output_dir, "2_bar_vector_risk.html")
    fig_bar.write_html(path_bar)
    generated_files.append(path_bar)

    # ==========================================
    # CHART 3: HISTOGRAM (Temperature Frequency Distribution)
    # ==========================================
    fig_hist = px.histogram(
        df, x="temperature_2m", nbins=15,
        title="<b>Figure 3: Environmental Frequency Distribution of Ambient Temperature</b>",
        labels={"temperature_2m": "Temperature (2m Height, °C)"},
        color_discrete_sequence=["#AB63FA"], # Amethyst Purple
        template="plotly_dark"
    )
    fig_hist.update_layout(bargap=0.1, yaxis_title="Hour Frequency Count")
    path_hist = os.path.join(output_dir, "3_histogram_temp.html")
    fig_hist.write_html(path_hist)
    generated_files.append(path_hist)

    # ==========================================
    # CHART 4: SCATTER PLOT (Temperature vs. Relative Humidity Matrix)
    # ==========================================
    fig_scatter = px.scatter(
        df, x="temperature_2m", y="relative_humidity_2m", color="vector_epidemiology_status", size="precipitation",
        title="<b>Figure 4: Bivariate Interaction Profile: Temperature vs. Relative Humidity Matrix</b>",
        labels={"temperature_2m": "Temperature (°C)", "relative_humidity_2m": "Relative Humidity (%)", 
                "vector_epidemiology_status": "Risk Evaluation", "precipitation": "Precipitation Size (mm)"},
        color_discrete_map={
            "High Proliferation Risk (Optimal Vector Lifecycle)": "#FF6692",
            "Moderate Risk (Sustained Vector Activity)": "#B6E880",
            "Low Risk (Suppressed Vector Activity)": "#19D3F3"
        },
        template="plotly_dark"
    )
    path_scatter = os.path.join(output_dir, "4_scatter_climate_matrix.html")
    fig_scatter.write_html(path_scatter)
    generated_files.append(path_scatter)

    # ==========================================
    # CHART 5: PIE CHART (Molecular Cellular Stress Proportions)
    # ==========================================
    fig_pie = px.pie(
        df, names="cellular_mutagenic_status",
        title="<b>Figure 5: Proportional Genomic Stress Allocations across Timeline</b>",
        color="cellular_mutagenic_status",
        color_discrete_map={
            "Severe Stress (Upregulation of NER Pathways & Thymine Dimer Repair)": "#EF553B",
            "Moderate Stress (Standard ROS Neutralization Active)": "#FECB52",
            "Baseline (Minimal Cellular Radiation Stress)": "#636EFA"
        },
        template="plotly_dark"
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    path_pie = os.path.join(output_dir, "5_pie_stress_allocation.html")
    fig_pie.write_html(path_pie)
    generated_files.append(path_pie)

    # ==========================================
    # CHART 6: STACKED AREA CHART (Advanced Metric)
    # ==========================================
    fig_area = px.area(
        df, x="time", y="uv_index",
        title="<b>Figure 6: Cumulative Area Projection of Radiative Flux</b>",
        labels={"time": "Timeline", "uv_index": "UV Index Intensity"},
        color_discrete_sequence=["#FF97FF"], # Soft Orchid
        template="plotly_dark"
    )
    path_area = os.path.join(output_dir, "6_area_radiation_flux.html")
    fig_area.write_html(path_area)
    generated_files.append(path_area)

    # ==========================================
    # CHART 7: BOX PLOT (Advanced Metric)
    # ==========================================
    fig_box = px.box(
        df, x="vector_epidemiology_status", y="relative_humidity_2m", color="vector_epidemiology_status",
        title="<b>Figure 7: Variance Profile: Relative Humidity Stability Box Plot</b>",
        labels={"vector_epidemiology_status": "Risk Status", "relative_humidity_2m": "Relative Humidity Dispersion (%)"},
        template="plotly_dark"
    )
    path_box = os.path.join(output_dir, "7_box_humidity_variance.html")
    fig_box.write_html(path_box)
    generated_files.append(path_box)

    # ==========================================
    # CHART 8: 2D DENSITY HEATMAP (Advanced Metric)
    # ==========================================
    fig_heatmap = px.density_heatmap(
        df, x="temperature_2m", y="relative_humidity_2m",
        title="<b>Figure 8: 2D Density Cluster Map: Microclimate Spatial Heatmap</b>",
        labels={"temperature_2m": "Temperature Coordinates (°C)", "relative_humidity_2m": "Relative Humidity Matrix (%)"},
        color_continuous_scale="Viridis",
        template="plotly_dark"
    )
    path_heatmap = os.path.join(output_dir, "8_density_heatmap.html")
    fig_heatmap.write_html(path_heatmap)
    generated_files.append(path_heatmap)

    # ==========================================
    # TERMINAL AUTOMATION EXECUTION
    # ==========================================
    print(f"\n🎉 Success! All 8 graphs compiled and saved to the folder: '{output_dir}/'")
    
    # Automatically boot up the main line timeline chart in your browser right away
    main_chart_url = os.path.abspath(generated_files[0])
    print(f"🌐 Launching primary interactive dashboard chart: file://{main_chart_url}")
    webbrowser.open(f"file://{main_chart_url}")

if __name__ == "__main__":
    run_vs_code_dashboard()